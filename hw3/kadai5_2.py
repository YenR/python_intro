# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:04:06 2019

@author: u593120c
"""

# 課題5-2:
# weight-height.csvの男性／女性の体重／身長（いずれかでよい）
# 、marathon_results.csvの時間(time)のデータがそれぞれ正規分布に従うかカイ二乗検定により判定せよ。
# ただし、データの標準化には課題4-2で作成した関数を用いよ。
# また、求めた𝜒2に対するp値は、モジュールscipy.statsを用いて求めてよい。※𝜒2分布の自由度に注意せよ。

import pandas as pd
import random
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np
from collections import Counter
from scipy.stats import chi2
import statistics
import kadai5_1

# sample size
N = 1000
# repetitions
M = 1000


# standardize data by subtracting mean and dividing by std dev
def standardize(data):
    mean = statistics.mean(data)
    stddev = statistics.stdev(data)
    new = []
    for i in data:
        new.append( (i - mean) / stddev )
    return new


def main():
    data = pd.read_csv('weight-height.csv')
    m_height = data[data.Gender == 'Male']['Height'].tolist()
    # m_weight = data[data.Gender == 'Male']['Weight'].tolist()

    data2 = pd.read_csv('marathon_results.csv')
    m_time = data2[data2.gender == 'M']['time'].tolist()
    # m_weight = data[data2.gender == 'F']['time'].tolist()

    m_height = standardize(m_height)
    m_time = standardize(m_time)

    kai_list = []
    for i in range(M):
        num_list = random.sample(m_height, N)
        kai_list.append(kadai5_1.chi_square(num_list))
    kadai5_1.draw_chi_test(kai_list, "Chi-Square Test using Male Height Data", k=11, bins2=range(1,50))

    kai_list2 = []
    for i in range(M):
        num_list = random.sample(m_time, N)
        kai_list2.append(kadai5_1.chi_square(num_list))
    kadai5_1.draw_chi_test(kai_list2, "Chi-Square Test using Male Time Data", k=95, bins2=range(40,140))

    # TODO: magic numbers?


if __name__ == "__main__":
    main()
