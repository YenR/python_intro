# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:07:12 2019

@author: u593120c
"""


import pandas as pd
import matplotlib.pyplot as plt
import random
import statistics
import numpy as np

# number of samples
N = 10
# learning rate = 学習率 for gradient descent algorithm = 最急降下法
alpha = 0.1
# starting variables = 初期値
a_start = 1.0
b_start = 1.0
# margin of error
precision = 0.005
# maximum number of iterations
max_iterations = 1000

def plot_hw(h, w):
    plt.figure()
    plt.scatter(h, w, c='blue', alpha=0.5, label='data')
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.show()


def standardize(data):
    mean = statistics.mean(data)
    stddev = statistics.stdev(data)
    new = []
    for i in data:
        new.append( (i - mean) / stddev )
    return new


# MSE = (1 / N) * Sum (weighti - (a * heighti +　b))^2
def mse(weights, heights, a, b):
    sum = 0.0
    for x in zip(weights,heights):
        sum += (x[0] - (a * x[1] + b)) ** 2
    return sum / len(weights)


def kadai4_5koushin(x, y, w):
    return w - alpha * fdw(x,y,w)

def gradient_descent(weights, heights, a, b):
    graph_data = []

    xi = [np.array([xx, 1]).T for xx in weights]
    x = np.array(xi).T
    w = np.array([[a, b]]).T
    y = np.asarray(heights).T

    for i in range(max_iterations):
        #graph_data.append(mse(weights, heights, a, b))
        new_w = kadai4_5koushin(x, y, w)
        if abs(np.sum(w - new_w)) < precision :
            break
        w = new_w

    #plot_descent(graph_data)
    return w


def plot_hw_withline(h, w, a, b):
    plt.figure()

    x = range(-2,3,1)
    y = [a * xi + b for xi in x]

    plt.plot(x, y, '-b', label='y=ax+b')
    plt.scatter(h, w, c='blue', alpha=0.5, label='data')
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.show()


# derivative for w = 1/N * XT * (Xw - y)
def fdw(x,y,w):
    return (1 / x.shape[0]) * x.T * (x * w - y)


def main():

    data = pd.read_csv('weight-height.csv')
    m_height= data[data.Gender=='Male']['Height'].tolist()
    m_weight= data[data.Gender=='Male']['Weight'].tolist()
    m_sample = random.sample(list(zip(m_height, m_weight)), N)
    m_sample_height = [m[0] for m in m_sample]
    m_sample_weight = [m[1] for m in m_sample]
    m_sample_height = standardize(m_sample_height)
    m_sample_weight = standardize(m_sample_weight)

    # 課題4-5:
    # 課題4-4において、xi = (xi, 1)T, w = (a,b)T, X = (x1, ...xn)T, y = (y1, ...yn)Tとおくと、
    # f(w) = (1/2N) * ||Xw - y|| ** 2
    # f'(w) = 1/N * XT * (Xw - y)となり、
    # w = w - alpha * f'(w) により更新すればよい。
    # モジュールnumpyを用いて課題4-4の更新部分を変更し、課題4-4と動作が同じとなるか検証せよ。

    w = gradient_descent(m_sample_weight, m_sample_height, a_start, b_start)

    #plot_hw_withline(m_sample_height, m_sample_weight, a, b)
    print(w)



    # 課題4-7:
    # numpyのpolyfitメソッドにより、
    # a, b = np.polyfit(x, y, 1)
    # のようにMSEを最小化するa、bを求められる。
    # この解と比較し、課題4-4、4-5、4-6の動作検証をせよ。


if __name__ == "__main__":
    main()