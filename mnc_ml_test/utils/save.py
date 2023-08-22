import torch
import matplotlib.pyplot as plt


def save_model(stamp, epochs, model, optimizer, loss):
    torch.save({
        'epoch': epochs,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': loss,
    }, 'output/train/' + stamp + '-model.pth')

def save_plots(stamp, train_loss, valid_loss, train_metric, valid_metric):
    plt.figure(figsize=(10, 7))
    plt.plot(train_loss, color='blue', linestyle='-', label='train loss')
    plt.plot(valid_loss, color='red',  linestyle='-', label='valid loss')
    plt.plot(train_metric, color='green', linestyle='-', label='train loss')
    plt.plot(valid_metric, color='yellow',  linestyle='-', label='valid loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.ylim(0.0, 0.02)
    plt.legend()
    plt.savefig('output/train/' + stamp + '-loss.png')
