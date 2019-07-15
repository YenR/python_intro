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
from scipy.stats import chi2
from scipy.stats import chi
from scipy.stats import norm
import statistics
import scipy.stats
import numpy as np
import random
import matplotlib.pyplot as plt

import kadai5_1

# sample size
N = 1000

bins = [i/10 for i in range(-50,50)]


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

    data2 = pd.read_csv('marathon_results.csv')
    m_time = data2[data2.gender == 'M']['time'].tolist()

    time_sample = random.sample(m_time, N)
    height_sample = random.sample(m_height, N)

    height_sample = standardize(height_sample)
    time_sample = standardize(time_sample)

    binplace_height = np.digitize(height_sample, bins)
    binplace_time = np.digitize(time_sample, bins)

    norms = []
    observations_height = []
    observations_time = []

    for i in range(0, len(bins)-1):
        norms.append((norm.cdf(bins[i+1]) - norm.cdf(bins[i])) * N / 100)
        temp, = np.where(binplace_height == i+1)
        observations_height.append(temp.size / 100)
        temp, = np.where(binplace_time == i+1)
        observations_time.append(temp.size / 100)

    print("-- Results of scipy chisquare test --")
    print(scipy.stats.chisquare(f_obs=observations_height, f_exp=norms, ddof=3))
    print(scipy.stats.chisquare(f_obs=observations_time, f_exp=norms, ddof=3))

    print("-- Results of own chi square test --")
    print(kadai5_1.chi_square(height_sample))
    print(kadai5_1.chi_square(time_sample))

    # add one more 0 for easier plotting
    norms.append(0)
    observations_height.append(0)
    observations_time.append(0)
    # plot
    plt.plot(bins, observations_height, label="Height")
    plt.plot(bins, observations_time, label="Time")
    plt.plot(bins, norms, label="Normal")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
