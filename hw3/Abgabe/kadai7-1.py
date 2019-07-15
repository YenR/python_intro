# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:04:06 2019

@author: u593120c
"""

import pandas as pd
import statistics
import random
import matplotlib.pyplot as plt
import numpy as np, scipy.stats as st


Ns = [(50 + 250 * i) for i in range(0,13)]
M = 1000

def main():
    
    # 課題7-1:
    # marathon_results.csvの時間(time)はあるマラソンにおける各選手のタイムである。
    # 一部の選手からこのマラソンにおける平均タイムを求めることを考える。
    # N個のランダムに抽出した選手の平均タイムを得る（標本平均）。
    # これをM回繰り返し、標本平均の平均と標準偏差を算出せよ。
    # Nを変化させ、各Nに対して得られたM個の平均が正規分布に従うか、課題5-2と同様にカイ二乗検定により判定せよ。
    # また、標本平均が正規分布に従うとき、その平均及びその95%信頼区間をエラーバー付きグラフで示せ。
    # また、全選手の平均タイム（母平均）を同じグラフに表示し、それらの関係について考察せよ。

    data = pd.read_csv('marathon_results.csv')
    time = data['time'].tolist()

    population_mean = statistics.mean(time)
    plt.plot(Ns, [population_mean] * 13, 'ro-')
    
    collect_means = []

    for n in Ns:
        means = []
        for i in range(M):
            sample = random.sample(time, n)
            mean = statistics.mean(sample)
            means.append(mean)

        mean = statistics.mean(means)
        stdev = statistics.stdev(means)
        collect_means.append(mean)
        
        # TODO: check if mean fits chi square test

        lower_limit = mean - 1.96 * stdev
        upper_limit = mean + 1.96 * stdev

        plt.plot((n, n), (lower_limit, upper_limit), 'b-')
        
        print("Samples: " + str(n) + ", mean: " + str(mean) + ", stdev: " + str(stdev))
        
    
    plt.plot(Ns, collect_means, 'b-')
    plt.legend(('Population Mean', 'Sample mean and 95% confidence interval'), loc='upper right')
    plt.title("Marathon result means, M = " + str(M))
    plt.xlabel('Sample Size')
    plt.ylabel('Time')
    plt.show()
    
    

if __name__ == "__main__":
    main()