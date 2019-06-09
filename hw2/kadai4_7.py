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


# 課題4-7:
# numpyのpolyfitメソッドにより、
# a, b = np.polyfit(x, y, 1)
# のようにMSEを最小化するa、bを求められる。
# この解と比較し、課題4-4、4-5、4-6の動作検証をせよ。
def k4_7(weights, heights):

    x = np.array(weights)
    y = np.array(heights)
    a, b = np.polyfit(x, y, 1)

    return a, b


def main():
    data = pd.read_csv('weight-height.csv')
    m_height= data[data.Gender=='Male']['Height'].tolist()
    m_weight= data[data.Gender=='Male']['Weight'].tolist()
    m_sample = random.sample(list(zip(m_height, m_weight)), N)
    m_sample_height = [m[0] for m in m_sample]
    m_sample_weight = [m[1] for m in m_sample]
    m_sample_height = standardize(m_sample_height)
    m_sample_weight = standardize(m_sample_weight)

    a, b = k4_7(m_sample_weight, m_sample_height)
    plot_hw_withline(m_sample_height, m_sample_weight, a, b)


if __name__ == "__main__":
    main()
