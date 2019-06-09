# -*- coding: utf-8 -*-
"""

@author: Tom Tucek トゥチェク・トム
"""


import pandas as pd
import matplotlib.pyplot as plt
import random
import statistics
import numpy as np

# number of samples
N = 100
# learning rate = 学習率 for gradient descent algorithm = 最急降下法
alpha = 0.1
# starting variables = 初期値
a_start = 1.0
b_start = 1.0
# margin of error
precision = 0.0005
# maximum number of iterations
max_iterations = 1000


# standardize data by subtracting mean and dividing by std dev
def standardize(data):
    mean = statistics.mean(data)
    stddev = statistics.stdev(data)
    new = []
    for i in data:
        new.append( (i - mean) / stddev )
    return new


# plot graph together with MSE line reaching from x = -2 to 2
def plot_hw_withline(h, w, a, b):
    plt.figure()
    # calculate y using arguments a and b
    x = range(-2,3,1)
    y = [a * xi + b for xi in x]

    plt.plot(x, y, '-b', label='y=ax+b')
    plt.scatter(h, w, c='blue', alpha=0.5, label='data')
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.show()


# 最急降下法

# 課題4-5:
# 課題4-4において、xi = (xi, 1)T, w = (a,b)T, X = (x1, ...xn)T, y = (y1, ...yn)Tとおくと、
# f(w) = (1/2N) * ||Xw - y|| ** 2
# f'(w) = 1/N * XT * (Xw - y)となり、
# w = w - alpha * f'(w) により更新すればよい。
# モジュールnumpyを用いて課題4-4の更新部分を変更し、課題4-4と動作が同じとなるか検証せよ。
def k4_5(weights, heights, a = a_start, b = b_start):
    w = np.array([[a_start, b_start]]).T
    X = np.array([[xx, 1] for xx in weights])
    y = np.asarray([heights]).T
    
    for i in range(max_iterations):
        new_w = kadai4_5koushin(X, y, w)
        if abs(np.sum(w - new_w)) < precision :
            break
        w = new_w

    return float(w[0]), float(w[1])


# update function for 4-5
def kadai4_5koushin(X, y, w):
    return w - alpha * fdw(X,y,w)


# derivative for w = 1/N * XT * (Xw - y)
def fdw(X,y,w):
    return (1 / X.shape[0]) * np.dot(X.T, np.dot(X,w)-y)


def main():
    data = pd.read_csv('weight-height.csv')
    m_height= data[data.Gender=='Male']['Height'].tolist()
    m_weight= data[data.Gender=='Male']['Weight'].tolist()
    m_sample = random.sample(list(zip(m_height, m_weight)), N)
    m_sample_height = [m[0] for m in m_sample]
    m_sample_weight = [m[1] for m in m_sample]
    m_sample_height = standardize(m_sample_height)
    m_sample_weight = standardize(m_sample_weight)

    a,b = k4_5(m_sample_weight, m_sample_height)
    plot_hw_withline(m_sample_height, m_sample_weight, a, b)


if __name__ == "__main__":
    main()