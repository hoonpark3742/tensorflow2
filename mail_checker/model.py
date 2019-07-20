import mglearn
import matplotlib.pyplot as plt
from mglearn.datasets import make_wave
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
import numpy as np


class KnnModel:
    def __init__(self):
        x, y = make_wave(n_samples=40)
        self.x_train, self.x_test, self.y_train, self.y_test = \
            train_test_split(self.x, self.y, random_state=0, test_sixe = 0.3)
        self.knn_reg = KNeighborsRegressor(n_neighbors=3, n_jobs=-1)
        # n_jobs=-1 : n_jobs 사용할 코어의 수, -1 == all
        self.knn_reg.fit(self.x_train, self.y_train)

    def create_model(self):
        _, axes = plt.subplot(1, 3)
        line = np.linspace(-5, 5, num=1000)
        line = line.reshape(-1, 1)

        # for i, ax in zip([1, 3, 9], axes.ravel()):