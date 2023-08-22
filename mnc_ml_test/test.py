import torch
import torch.nn as nn
import torch.optim as optim
from utils.dataloader import DataLoader
from utils.save import *
from model.MLNet import MultiLinearNet

import time
import datetime
import numpy as np
import pandas as pd

def test(dataloader, model):
    model.eval()
    with torch.no_grad():
        pred_list = []
        for batch, data in enumerate(dataloader):
            x, y = data[:, :11], data[:, -1:]
            x, y = x.to(device), y.to(device)

            pred = model(x)
            pred_list.append(pred)
    return pred_list

def main():
    pd.set_option("display.max_columns", None)
    dataset = DataLoader("./data/test.csv")
    df = dataset.df
    ori_df = df.copy()

    df["X6"]  = df["X0"] / df["X0"]
    df["X7"]  = df["X1"] / df["X0"]
    df["X8"]  = df["X2"] / df["X0"]
    df["X9"]  = df["X3"] / df["X0"]
    df["X10"] = df["X4"] / df["X0"]
    df["X11"] = df["X5"] / df["X0"]

    df = df[["X0", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "target"]]
    df = dataset.normilize(df, mode=True)
    df["X6"] = 0.0

    # df.drop(["X1", "X5", "X6", "X2", "X3", "X4"], axis=1, inplace=True)
    df.drop(["X6"], axis=1, inplace=True)
    test_data = torch.FloatTensor(df.values)
    batch_size = 32
    test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size, shuffle=False)

    model = MultiLinearNet().to(device)

    checkpoint = torch.load("./output/train/20221128-1147-model.pth")
    model.load_state_dict(checkpoint['model_state_dict'])

    pred_list = test(test_loader, model)

    output = torch.cat(pred_list, 0)
    output_df = pd.DataFrame(output.numpy())
    ori_df["target"] = output_df
    print(ori_df)
    ori_df.to_csv("./output/test/test.csv", index=False)


if __name__ == "__main__":
    if torch.cuda.is_available():
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')
    main()
