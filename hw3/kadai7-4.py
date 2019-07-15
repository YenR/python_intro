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

N = 100
M = 10000

def main():

    # 課題7-4:
    # 課題7-1～7-3の結果を踏まえ、適当な人数の選手のタイムを抽出し、平均タイムとその95%信頼区間を算出せよ。
    # これを何回も（10000回など）繰り返し、全選手の平均タイムが求めた信頼区間に入らない割合を出力せよ（約5%となるはず）。

    data = pd.read_csv('marathon_results.csv')
    time = data['time'].tolist()

    population_mean = statistics.mean(time)

    misses = 0

    for i in range(M):
        sample = random.sample(time, N)
        mean = statistics.mean(sample)
        stdev = statistics.stdev(sample)

        # code from https://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data
        lower_limit, upper_limit = st.t.interval(0.95, len(sample) - 1, loc=np.mean(sample), scale=st.sem(sample))

        within_interval = True
        if population_mean < lower_limit or population_mean > upper_limit:
            within_interval = False
            misses += 1

        #print(("O" if within_interval else "X"), "Sample statistics: Mean = ", mean, ", Stdev = ", stdev,
        #      ", 95% Confidence Interval = [", lower_limit, ", ", upper_limit, "]")

        if(i%int(M/100) == 0):
            print("Calculations at ", str(i/M * 100), "%")

    print("Ratio of misses: ", str(misses/M * 100), "%")


if __name__ == "__main__":
    main()