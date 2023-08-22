import torch
import torch.nn as nn

class MAELoss(nn.Module):
    def __init__(self):
        super(MAELoss, self).__init__()

    def forward(self, pred, target):
        return torch.mean(torch.abs(pred - target))