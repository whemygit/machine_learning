#!/usr/bin/env python
# -- coding: utf-8 --
import sys
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris

reload(sys)
sys.setdefaultencoding("utf-8")

def create_data(n):
    np.random.seed(1)
    x_11=np.random.randint(0,100,(n,1))
    x_12 = np.random.randint(0, 100, (n, 1))
    x_13 = np.random.randint(0, 100, (n, 1))
    x_21 = np.random.randint(0, 100, (n, 1))
    x_22 = np.random.randint(0, 100, (n, 1))
    x_23 = np.random.randint(0, 100, (n, 1))

    new_x_12=x_12*np.sqrt(2)/2-x_13*np.sqrt(2)/2
    new_x_13 = x_12 * np.sqrt(2) / 2 - x_13 * np.sqrt(2) / 2
    new_x_22 = x_22 * np.sqrt(2) / 2 - x_23 * np.sqrt(2) / 2
    new_x_23 = x_22 * np.sqrt(2) / 2 - x_23 * np.sqrt(2) / 2

    plus_samples=np.hstack([x_11,new_x_12,new_x_13,np.ones((n,1))])
    minus_samples=np.hstack([x_21,new_x_22,new_x_23,-np.ones((n,1))])




if __name__ == '__main__':
    pass