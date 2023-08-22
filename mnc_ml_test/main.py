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

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics


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
    df["X6"] = 1.0

    x = df.iloc[:, :12]
    y = df.iloc[:, -1:]

    randomforest_model = RandomForestRegressor()
    # pred = randomforest_model.predict(x)
    mae_score = metrics.make_scorer(mean_absolute_error, greater_is_better=False)

    rf_params = {'random_state': [2, 4, 6], 'n_estimators': [10, 20, 40, 60, 80, 100, 120, 140], 'criterion': ['absolute_error']}
    gridsearch_random_forest_model = GridSearchCV(estimator=randomforest_model,
                                                  param_grid=rf_params,
                                                  scoring=mae_score,
                                                  cv=5)
    gridsearch_random_forest_model.fit(x, y)
    print('최적 파라미터: ', gridsearch_random_forest_model.best_params_)

    pred = gridsearch_random_forest_model.best_estimator_.predict(x)
    print(f"loss: {mean_absolute_error(y_true=y, y_pred=pred)}")

if __name__ == "__main__":
    main()

