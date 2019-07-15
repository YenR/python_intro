# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:04:06 2019

@author: u593120c
"""


import pandas as pd
import math
import statistics
import random
import matplotlib.pyplot as plt


Ns = range(5,1001,5)
M = 50

def main():
    # 課題7-3:
    # N人の選手のタイムの標準偏差と母標準偏差𝜎を比較する。これらの差をM回算出し、その平均をグラフにプロットせよ。
    
    data = pd.read_csv('marathon_results.csv')
    time = data['time'].tolist()

    population_stdev = statistics.stdev(time)

    collect_difs = []

    for n in Ns:

        stdevs = []

        for i in range(M):
            sample = random.sample(time, n)
            stdev = abs(statistics.stdev(sample) - population_stdev)
            stdevs.append(stdev)

        collect_difs.append(statistics.mean(stdevs))
        
        print("Samples: " + str(n))

    plt.plot(Ns, collect_difs, 'b-')
    plt.xlabel('Sample Size')
    plt.ylabel('Diff between Population Std and Sample Std')

    plt.show()


if __name__ == "__main__":
    main()