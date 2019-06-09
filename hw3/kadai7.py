# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:04:06 2019

@author: u593120c
"""

# 課題7-1:
# marathon_results.csvの時間(time)はあるマラソンにおける各選手のタイムである。
# 一部の選手からこのマラソンにおける平均タイムを求めることを考える。
# N個のランダムに抽出した選手の平均タイムを得る（標本平均）。
# これをM回繰り返し、標本平均の平均と標準偏差を算出せよ。
# Nを変化させ、各Nに対して得られたM個の平均が正規分布に従うか、課題5-2と同様にカイ二乗検定により判定せよ。
# また、標本平均が正規分布に従うとき、その平均及びその95%信頼区間をエラーバー付きグラフで示せ。
# また、全選手の平均タイム（母平均）を同じグラフに表示し、それらの関係について考察せよ。

# 課題7-2:
# 標本平均の標準偏差である標準誤差は、母標準偏差𝜎により、𝑆𝐸=𝜎𝑁で求められる。
# 全選手のタイムの標準偏差𝜎を用いて、各Nに対する標準誤差𝑆𝐸を求め、課題7-1で得た、
# 各Nに対して得られたM個の標本平均の標準偏差とと共にグラフに表示し、比較せよ。

# 課題7-3:
# N人の選手のタイムの標準偏差と母標準偏差𝜎を比較する。これらの差をM回算出し、その平均をグラフにプロットせよ。

# 課題7-4:
# 課題7-1～7-3の結果を踏まえ、適当な人数の選手のタイムを抽出し、平均タイムとその95%信頼区間を算出せよ。
# これを何回も（10000回など）繰り返し、全選手の平均タイムが求めた信頼区間に入らない割合を出力せよ（約5%となるはず）。

import pandas as pd
import statistics
import random

N = 1000
M = 1000

def main():

    data = pd.read_csv('marathon_results.csv')
    #m_time = data2[data2.gender == 'M']['time'].tolist()
    #f_time = data[data2.gender == 'F']['time'].tolist()
    time = data['time'].tolist()

    means = []
    for i in range(M):
        sample = random.sample(time, N)
        mean = statistics.mean(sample)
        means.append(mean)

    print(statistics.mean(means))
    print(statistics.stdev(means))

    print(statistics.mean(time))

if __name__ == "__main__":
    main()