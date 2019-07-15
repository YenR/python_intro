# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:04:06 2019

@author: u593120c
"""

# 課題6-1:
# 右図のような1×1の正方形内にランダムに点を打ち、原点から距離が１以下の点（半円内に入る）の割合を算出する。
# 半円の面積がΤ𝜋4、正方形の面積が1なので、算出した割合×4=𝜋となる。点数Nを与えると𝜋の推定値を出力する関数を作成せよ。

# 課題6-2:
# N個の点を打ち、𝜋を推定することをM回繰り返し、推定値𝜋が正規分布に従うか課題5-2と同様に判定せよ。
# 正規分布に従うとき、95%信頼区間の幅が求める精度を満たすまでNを増やし、
# Nによる平均と95%信頼区間の変化をエラーバー付きグラフで示せ。

import math
import random
import numpy as np
import statistics
import matplotlib.pyplot as plt
from scipy.stats import norm

origin = np.array((0,0))
M = 7


def approximate_pi(n):
    hits = 0
    for i in range(n):
        point = np.array((random.random(), random.random()))
        if np.linalg.norm(point - origin) <= 1:
            hits += 1
    return (hits/n) * 4


def main():
    points = [1000 * (2 ** i) for i in range(0,8)]

    plt.xscale("log")
    plt.plot(points, [math.pi] * 8, 'ro-')

    means = []

    for i in points:
        collect = []
        for j in range(M):
            collect.append(approximate_pi(i))

        mean = statistics.mean(collect)
        stdev = statistics.stdev(collect)

        # TODO: 95% confidence interval? ok with this?
        lower_limit = mean - 2 * stdev
        upper_limit = mean + 2 * stdev

        plt.plot((i, i), (lower_limit, upper_limit), 'b-')
        print("Points: " + str(i) + ", mean: " + str(mean) + ", stdev: " + str(stdev))

        #print("plotted: " + str(lower_limit) + " to " + str(upper_limit))
        #prob = norm.cdf(x=mean + 2 * stdev, loc=mean, scale=stdev) \
        #       - norm.cdf(x=mean - 2 * stdev, loc=mean, scale=stdev)
        #print(prob)

        means.append(mean)

    plt.plot(points, means, 'b-')
    plt.title("Simulating PI, M = " + str(M))
    plt.show()

if __name__ == "__main__":
    main()