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
N = 100
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


# derivative for a = (1 / N) * Sum (xi * ((a * xi + b) - yi))
def fda(weights, heights, a, b):
    sum = 0.0
    for x in zip(weights,heights):
        sum += x[0] * ((a * x[0] + b) - x[1])
    return sum / len(weights)


# derivative for b = (1 / N) * Sum (((a * xi + b) - yi))
def fdb(weights, heights, a, b):
    sum = 0.0
    for x in zip(weights,heights):
        sum += (a * x[0] + b) - x[1]
    return sum / len(weights)


def plot_descent(data):
    plt.figure("gradient descent")
    plt.plot(data)
    plt.xlabel("iterations")
    plt.ylabel("MSE")
    plt.show()


def kadai4_4koushin(weights, heights, a, b):
    a -= fda(weights, heights, a, b) * alpha
    b -= fdb(weights, heights, a, b) * alpha
    return a,b


def gradient_descent(weights, heights, a, b, method = kadai4_4koushin):
    graph_data = []
    for i in range(max_iterations):
        graph_data.append(mse(weights, heights, a, b))
        new_a, new_b = method(weights, heights, a, b)
        if abs(a - new_a) < precision and abs(b - new_b) < precision:
            break
        a, b = new_a, new_b
    plot_descent(graph_data)
    return a,b


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


def kadai4_5koushin(weights, heights, a, b):

    xi = [np.array([xx,1]).T for xx in weights]
    w = np.array([[a,b]]).T
    x = np.array(xi)
    y = np.array([heights]).T

    w = w - alpha * fdw(x,y,w)

    return w.item((0,0)), w.item((1,0))

# derivative for w = 1/N * XT * (Xw - y)
def fdw(x,y,w):
    return (1 / x.shape[0]) * x.T * (x * w - y)


def main():

    # 課題4-1:
    # weight-height.csvから男性もしくは女性の身長、体重の対をN個ランダムに抽出し、プロットせよ。
    data = pd.read_csv('weight-height.csv')
    m_height= data[data.Gender=='Male']['Height'].tolist()
    m_weight= data[data.Gender=='Male']['Weight'].tolist()
    
    m_sample = random.sample(list(zip(m_height, m_weight)), N)
    m_sample_height = [m[0] for m in m_sample]
    m_sample_weight = [m[1] for m in m_sample]
    plot_hw(m_sample_height, m_sample_weight)

    # 課題4-2:
    # データを平均と標準偏差を用いて標準化する関数を作成し、課題4-1の身長、体重データをそれぞれ標準化してプロットせよ。

    m_sample_height = standardize(m_sample_height)
    m_sample_weight = standardize(m_sample_weight)
    plot_hw(m_sample_height, m_sample_weight)

    print(mse(m_sample_height, m_sample_weight, -10, -10))

    # 課題4-3:
    # weight = a×ℎeight+b という式により、身長から体重を推定することを考える。
    # 推定値の正しさを以下の式で評価する。
    # MSE = (1 / N) * Sum (weighti - (a * heighti +　b))^2
    # N人の身長と体重、及びa、bが与えられたとき、MSEを出力する関数を作成せよ。

    # 課題4-4:
    # MSEを最小化するa、bを最急降下法により求める。
    # a、bを一回更新する関数を作成し、反復更新によりMSEを十分小さくするa、bを求めるプログラムを作成せよ。
    # 課題4 - 2のデータを用い、a、bの初期値や学習率を変化させ、動作検証せよ。

    a,b = gradient_descent(m_sample_weight, m_sample_height, a_start, b_start)
    plot_hw_withline(m_sample_height, m_sample_weight, a, b)


if __name__ == "__main__":
    main()