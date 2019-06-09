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
precision = 0.005
# maximum number of iterations
max_iterations = 1000


# plot given data points
def plot_hw(h, w):
    plt.figure()
    plt.scatter(h, w, c='blue', alpha=0.5, label='data')
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.legend()
    plt.show()


# standardize data by subtracting mean and dividing by std dev
def standardize(data):
    mean = statistics.mean(data)
    stddev = statistics.stdev(data)
    new = []
    for i in data:
        new.append( (i - mean) / stddev )
    return new

# 課題4-3:
# weight = a×ℎeight+b という式により、身長から体重を推定することを考える。
# 推定値の正しさを以下の式で評価する。
# MSE = (1 / N) * Sum (weighti - (a * heighti +　b))^2
# N人の身長と体重、及びa、bが与えられたとき、MSEを出力する関数を作成せよ。
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


# descent graph showing changing MSE over iterations
def plot_descent(data):
    plt.figure("gradient descent")
    plt.plot(data)
    plt.xlabel("iterations")
    plt.ylabel("MSE")
    plt.show()


# 最急降下法
# includes return for MSE graph data
def k4_4_withMSE(weights, heights, a=a_start, b=b_start):
    graph_data = []
    for i in range(max_iterations):
        graph_data.append(mse(weights, heights, a, b))
        new_a, new_b = kadai4_4koushin(weights, heights, a, b)
        if abs(a - new_a) < precision and abs(b - new_b) < precision:
            break
        a, b = new_a, new_b
    #plot_descent(graph_data)
    return a,b, graph_data


# 最急降下法
# does not include return for MSE graph data
def k4_4(weights, heights, a=a_start, b=b_start):
    for i in range(max_iterations):
        new_a, new_b = kadai4_4koushin(weights, heights, a, b)
        if abs(a - new_a) < precision and abs(b - new_b) < precision:
            break
        a, b = new_a, new_b
    return a,b


# update function for 4-4
def kadai4_4koushin(weights, heights, a, b):
    a -= fda(weights, heights, a, b) * alpha
    b -= fdb(weights, heights, a, b) * alpha
    return a,b


# plot graph together with MSE line reaching from x = -2 to 2
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

    # 課題4-4:
    # MSEを最小化するa、bを最急降下法により求める。
    # a、bを一回更新する関数を作成し、反復更新によりMSEを十分小さくするa、bを求めるプログラムを作成せよ。
    # 課題4 - 2のデータを用い、a、bの初期値や学習率を変化させ、動作検証せよ。
    a,b,graph_data = k4_4_withMSE(m_sample_weight, m_sample_height)
    plot_descent(graph_data)
    plot_hw_withline(m_sample_height, m_sample_weight, a, b)


if __name__ == "__main__":
    main()