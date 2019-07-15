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
import statistics
import matplotlib.pyplot as plt

# number of repetitions for simulations
M = 50

# calculate distance of a point x,y to origin 0,0
def distance_to0(x,y):
    return math.sqrt(x ** 2 + y ** 2)

# simulate pi with n dots in a 1x1 square, calculate number of points within range = 1
def approximate_pi(n):
    hits = 0
    for i in range(n):
        x,y = random.random(), random.random()
        if distance_to0(x,y) <= 1: 
            hits += 1
    return (hits/n) * 4


def main():
    # use points in powers of 2 times 1000 (1000~128000)
    points = [1000 * (2 ** i) for i in range(0,8)]

    plt.xscale("log")
    plt.plot(points, [math.pi] * 8, 'ro-')

    means = []

    for i in points:
        collect = []
        
        # repeat simulation M times with given number of points
        for j in range(M):
            collect.append(approximate_pi(i))

        mean = statistics.mean(collect)
        stdev = statistics.stdev(collect)

        # 95% confidence interval
        lower_limit = mean - 1.96 * stdev
        upper_limit = mean + 1.96 * stdev

        plt.plot((i, i), (lower_limit, upper_limit), 'b-')
        
        print("Points: " + str(i) + ", mean: " + str(mean) + ", stdev: " + str(stdev))

        means.append(mean)

    plt.plot(points, means, 'b-')
    plt.title("Simulating PI, M = " + str(M))
    plt.show()
    

if __name__ == "__main__":
    main()