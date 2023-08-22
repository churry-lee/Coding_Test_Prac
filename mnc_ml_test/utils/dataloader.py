import matplotlib.pyplot as plt
import pandas as pd
import torch.utils.data
from typing import Dict, List, Tuple, Any
import numpy as np

class DataLoader(torch.utils.data.Dataset):
    def __init__(self, filepath: str):
        self.df = pd.read_csv(filepath, header=0, index_col=False)

    def __len__(self):
        return self.df.shape[0]


    def __getitem__(self, idx):
        X = self.df[self.df.columns[:6]].loc[idx]
        Y = self.df[self.df.columns[-1:]].loc[idx]
        return X, Y

    def normilize(self, df, mode: bool = False, method: str = "minmax"):
        len_col = len(df.columns)
        if mode:
            if method == "minmax":
                for idx in range(len_col - 1):
                    df.iloc[:, idx] = 2.0 * ((df.iloc[:, idx] - df.iloc[:, idx].min()) / (df.iloc[:, idx].max() - df.iloc[:, idx].min())) - 1.0
                    # df.iloc[:, idx] = (df.iloc[:, idx] - df.iloc[:, idx].min()) / (df.iloc[:, idx].max() - df.iloc[:, idx].min())
            elif method == "std":
                for idx in range(len_col):
                    df.iloc[:, idx] = (df.iloc[:, idx] - df.iloc[:, idx].mean()) / df.iloc[:, idx].std()
            else:
                for idx in range(len(df)):
                    df.iloc[idx] = (df.iloc[idx] - df.iloc[idx].min()) / (df.iloc[idx].max() - df.iloc[idx].min())
            return df
        else:
            return df



if __name__ == "__main__":
    pd.set_option("display.max_columns", None)
    dataset = DataLoader("../data/train.csv")
    df = dataset.df
    print(df.describe())

    df["X6"]  = df["X0"] / df["X0"]
    df["X7"]  = df["X1"] / df["X0"]
    df["X8"]  = df["X2"] / df["X0"]
    df["X9"]  = df["X3"] / df["X0"]
    df["X10"] = df["X4"] / df["X0"]
    df["X11"] = df["X5"] / df["X0"]
    corr_matrix = df.corr()
    print(corr_matrix["target"].sort_values(ascending=False))

    df = df[["X0", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "target"]]
    df = dataset.normilize(df, mode=True)
    df["X6"] = 0.0

    df.drop(["X1", "X5", "X6", "X2", "X3", "X4"], axis=1, inplace=True)

    print(df)
    print(len(df))


