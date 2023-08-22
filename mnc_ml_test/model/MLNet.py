import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import torch.nn as nn
import torch.nn.functional as F

class MultiLinearNet(nn.Module):
    def __init__(self):
        super(MultiLinearNet, self).__init__()

        # self.module = nn.Sequential(
        #     nn.Linear(12, 60, bias=True), nn.ELU(),
        #     nn.Linear(60, 60, bias=True), nn.ELU(),
        #     nn.Linear(60, 12, bias=True), nn.ELU(),
        #     nn.Linear(12, 6, bias=True), nn.ELU(),
        #     nn.Linear(6, 1, bias=True)
        # )
        # self.module = nn.Sequential(
        #     nn.Linear(11, 60, bias=True), nn.ELU(),
        #     nn.Linear(60, 60, bias=True), nn.ELU(),
        #     nn.Linear(60, 6, bias=True), nn.ELU(),
        #     nn.Linear(6, 1, bias=True)
        # )
        self.module = nn.Sequential(
            nn.Linear(6, 60, bias=True), nn.ELU(),
            nn.Linear(60, 60, bias=True), nn.ELU(),
            nn.Linear(60, 6, bias=True), nn.ELU(),
            nn.Linear(6, 1, bias=True)
        )

    def forward(self, x):
        x = self.module(x)
        return x
