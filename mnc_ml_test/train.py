import torch
import torch.nn as nn
import torch.optim as optim
from utils.dataloader import DataLoader
from utils.save import *
from model.MLNet import MultiLinearNet
from utils.loss_fn import MAELoss

import time
import datetime
import numpy as np
import pandas as pd

class WarmupConstantSchedule(torch.optim.lr_scheduler.LambdaLR):
    def __init__(self, optimizer, warmup_steps, last_epoch=-1):
        def lr_lambda(step):
            if step < warmup_steps:
                return float(step) / float(max(1.0, warmup_steps))
            return 1.

        super(WarmupConstantSchedule, self).__init__(optimizer, lr_lambda, last_epoch=last_epoch)

def train(dataloader, model, optimizer, loss_fn, metric_fn):
    model.train()
    batches = len(dataloader)
    train_loss_list, train_metric_list = [], []

    start_time = time.time()
    for batch, data in enumerate(dataloader):
        x, y = data[:, :6], data[:, -1:]
        x, y = x.to(device), y.to(device)

        optimizer.zero_grad()
        pred = model(x)
        loss = torch.sqrt(loss_fn(pred, y))
        metric = metric_fn(pred, y)
        loss.backward()
        optimizer.step()

        train_loss_list.append(loss.item())
        train_metric_list.append(metric.item())

        if (batch+1) % batches == 0:
            print(f'step: {batch+1}/{batches} | {time.time() - start_time:.2f} s/step | ', end='')
            print(f'train loss: {np.mean(train_loss_list):.6f} | metric: {np.mean(train_metric_list):.4f} | ', end='')

    return np.mean(train_loss_list), np.mean(train_metric_list)

def valid(dataloader, model, loss_fn, metric_fn):
    model.eval()
    with torch.no_grad():
        val_loss_list, val_metric_list = [], []
        for batch, data in enumerate(dataloader):
            x, y = data[:, :6], data[:, -1:]
            x, y = x.to(device), y.to(device)

            pred = model(x)
            val_loss = torch.sqrt(loss_fn(pred, y))
            val_metric = metric_fn(pred, y)

            val_loss_list.append(val_loss.item())
            val_metric_list.append(val_metric.item())

        print(f'valid loss: {np.mean(val_loss_list):.6f} | metric: {np.mean(val_metric_list):.4f}')

    return np.mean(val_loss_list), np.mean(val_metric_list)

def main():
    pd.set_option("display.max_columns", None)
    dataset = DataLoader("./data/train.csv")
    df = dataset.df

    df["X6"]  = df["X0"] / df["X0"]
    df["X7"]  = df["X1"] / df["X0"]
    df["X8"]  = df["X2"] / df["X0"]
    df["X9"]  = df["X3"] / df["X0"]
    df["X10"] = df["X4"] / df["X0"]
    df["X11"] = df["X5"] / df["X0"]

    df = df[["X0", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "target"]]
    df = dataset.normilize(df, mode=True)
    df["X6"] = 0.0

    df.drop(["X1", "X5", "X6", "X2", "X3", "X4"], axis=1, inplace=True)
    # df.drop(["X6"], axis=1, inplace=True)

    dataset = torch.FloatTensor(df.values)
    train_len = int(len(dataset) * 0.80)
    valid_len = int(len(dataset) * 0.20)
    train_data, valid_data = torch.utils.data.random_split(dataset, [train_len, valid_len])

    batch_size = 32
    train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True)
    valid_loader = torch.utils.data.DataLoader(valid_data, batch_size=batch_size, shuffle=True)

    model = MultiLinearNet().to(device)
    loss_fn = nn.MSELoss()
    # metric_fn = MAELoss()
    metric_fn = nn.L1Loss()

    learning_rate = 0.001
    # optimizer = optim.Adam(model.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-8, weight_decay=1e-5)
    optimizer = optim.AdamW(model.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-8, weight_decay=1e-5)
    # optimizer = optim.RMSprop(model.parameters(), lr=learning_rate)
    # optimizer = optim.RAdam(model.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-8, weight_decay=1e-5)
    # optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)

    # scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min')
    # scheduler = optim.lr_scheduler.LambdaLR(optimizer, lr_lambda = lambda epoch: 0.95 ** epoch)
    # scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=100, gamma=0.5)
    # scheduler = WarmupConstantSchedule(optimizer, 10)

    train_loss_list, valid_loss_list = [], []
    train_metric_list, valid_metric_list = [], []
    epochs = 3000
    for epoch in range(epochs):
        print(f'Epoch: {epoch+1}/{epochs} | ', end="")
        train_loss, train_metric = train(train_loader, model, optimizer, loss_fn, metric_fn)
        valid_loss, valid_metric = valid(valid_loader, model, loss_fn, metric_fn)
        # scheduler.step()

        train_loss_list.append(train_loss)
        valid_loss_list.append(valid_loss)
        train_metric_list.append(train_metric)
        valid_metric_list.append(valid_metric)

    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M")
    save_model(stamp, epochs, model, optimizer, loss_fn)
    save_plots(stamp, train_loss_list, valid_loss_list, train_metric_list, valid_metric_list)


if __name__ == "__main__":
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')
    print(f"Using Device: {device}")

    main()

