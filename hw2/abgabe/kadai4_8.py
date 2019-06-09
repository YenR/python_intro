# -*- coding: utf-8 -*-
"""

@author: Tom Tucek トゥチェク・トム
"""

import pandas as pd
import matplotlib.pyplot as plt
import random
import statistics
import numpy as np

import kadai4_1to4
import kadai4_5
import kadai4_6
import kadai4_7


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


# plot graph using 4 different methods from 4-4 to 4-7
def plot_4ways(h, w, title=""):
    a4, b4 = kadai4_1to4.k4_4(h, w)
    a5, b5 = kadai4_5.k4_5(h, w)
    a6, b6 = kadai4_6.k4_6(h, w)
    a7, b7 = kadai4_7.k4_7(h, w)

    plt.figure()
    # calculate y using arguments a and b
    x4 = x5 = x6 = x7 = range(int(min(h))-1, int(max(h)) + 2, 1)
    y4 = [a4 * xi + b4 for xi in x4]
    y5 = [a5 * xi + b5 for xi in x5]
    y6 = [a6 * xi + b6 for xi in x6]
    y7 = [a7 * xi + b7 for xi in x7]

    plt.plot(x4, y4, '-b', label='kadai 4')
    plt.plot(x5, y5, '-r', label='kadai 5')
    plt.plot(x6, y6, '-g', label='kadai 6')
    plt.plot(x7, y7, '-y', label='kadai 7')
    plt.scatter(h, w, c='blue', alpha=0.5, label='data')
    plt.xlabel("Height")
    plt.ylabel("Weight")
    plt.title(title)
    plt.legend()
    plt.savefig(title + ".png")
    plt.show()


def main():
    data = pd.read_csv('weight-height.csv')
    m_height= data[data.Gender=='Male']['Height'].tolist()
    m_weight= data[data.Gender=='Male']['Weight'].tolist()
    m_sample = random.sample(list(zip(m_height, m_weight)), N)
    m_sample_height = [m[0] for m in m_sample]
    m_sample_weight = [m[1] for m in m_sample]

    # calculate and draw plot using raw data
    plot_4ways(m_sample_height, m_sample_weight, "before standardizing")

    # standardize data
    m_sample_height = standardize(m_sample_height)
    m_sample_weight = standardize(m_sample_weight)

    # recalculate and redraw using standardized data
    plot_4ways(m_sample_height, m_sample_weight, "after standardizing")


if __name__ == "__main__":
    main()
