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


Ns = [(50 + 250 * i) for i in range(0,13)]
M = 100

def main():
    # 課題7-2:
    # 標本平均の標準偏差である標準誤差は、母標準偏差𝜎により、𝑆𝐸=𝜎𝑁で求められる。
    # 全選手のタイムの標準偏差𝜎を用いて、各Nに対する標準誤差𝑆𝐸を求め、課題7-1で得た、
    # 各Nに対して得られたM個の標本平均の標準偏差とと共にグラフに表示し、比較せよ。
    
    data = pd.read_csv('marathon_results.csv')
    time = data['time'].tolist()

    population_stdev = statistics.stdev(time)

    collect_SEs = []
    collect_SEp = []

    for n in Ns:
        means = []
        for i in range(M):
            sample = random.sample(time, n)
            mean = statistics.mean(sample)
            means.append(mean)

        stdev = statistics.stdev(means)
        SEp = population_stdev / math.sqrt(n)
        
        collect_SEs.append(stdev)
        collect_SEp.append(SEp)
        
        print("Samples: " + str(n) + ", stdev: " + str(stdev))

    plt.plot(Ns, collect_SEp, 'b-o')
    plt.plot(Ns, collect_SEs, 'r-x')
    plt.legend(('Standard Error', 'Std of ' +  str(M) + ' samples'), loc='upper right')
    plt.xlabel('Sample Size')
    plt.ylabel('Standard Deviation')

    plt.show()


if __name__ == "__main__":
    main()