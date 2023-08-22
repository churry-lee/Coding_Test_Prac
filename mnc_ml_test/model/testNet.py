import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import torch.nn as nn
import torch.nn.functional as F

class TestNet(nn.Module):
    def __init__(self, W, b):
        super(TestNet, self).__init__()
        self.weight = nn.Parameter(W)
        self.bias = nn.Parameter(b)

        self.fc1 = nn.Linear(11, 100, bias=True)
        self.fc2 = nn.Linear(100, 1, bias=True)


    def forward(self, x):
        # x = x.matmul(self.weight) + self.bias
        # output = F.relu(x)

        x = self.fc1(x)
        x = F.relu(x)
        x = self.fc2(x)

        return x
