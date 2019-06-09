# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:04:06 2019

@author: u593120c
"""

# 課題5-1:２回目課題の19枚目スライドを参考に、
# 平均0、分散1の正規分布に従う𝑁個の乱数を生成し、
# x2を計算せよ。
# これをM回繰り返し得られるx2の分布が、
# 自由度k−1のx2分布に近似するか確認せよ。
# 期待度数の算出には、モジュールscipy.statsを用いてよい。

import random
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
from collections import Counter
from scipy.stats import chi2


M = 1000  #試行回数
N = 1000  #データ数

bin_range = [(-10, -1.6), (-1.6, -1.2), (-1.2, -0.8), (-0.8, -0.4), (-0.4, 0), \
             (0, 0.4), (0.4, 0.8), (0.8, 1.2), (1.2, 1.6), (1.6, 10)]
bins = [x for (x,y) in bin_range]
bins.append(bin_range[9][1])


def chi_square(data):
    freq, _ = np.histogram(data, bins=bins)

    kai = []
    for i in range(0, 10):
        expect = norm.cdf(bin_range[i][1]) - norm.cdf(bin_range[i][0])
        kai.append((freq[i] ** 2) / (expect * N))
    return sum(kai) - N


def draw_chi_test(data, title="", k=10, bins2=range(70)):
    plt.hist(data, bins=bins2, density=True)  # ヒストグラムを描画
    plt.plot(bins2, chi2.pdf(bins2, k - 1))  # カイ2乗分布（自由度9）を描画
    plt.title(title)
    plt.show()


def main():
    kai_list = []
    for i in range(M):
        num_list = np.random.normal(loc=0, scale=1, size=N)
        kai_list.append(chi_square(num_list))
    draw_chi_test(kai_list, title="Chi-Square Test for Normal Distribution", bins2=range(50))


if __name__ == "__main__":
    main()
