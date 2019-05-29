# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:50:10 2019

@author: u593120c
"""

import random
import matplotlib.pyplot as plt
from scipy.stats import chi2
import numpy as np

M = 1000  #試行回数
N = 1000   #データ数

kai_list = []
for i in range(M):
    num_list = [random.randint(1,10) for x in range(N)] #N個の乱数生成
    bins=range(1,12)
    freq, _ = np.histogram(num_list, bins=bins) # ヒストグラムを作成
    kai = [(f**2)/(N/10) for f in freq]
    kai = sum(kai)-N
    kai_list.append(kai)
    
bins = range(70)
plt.hist(kai_list, bins=bins, density=True)  # ヒストグラムを描画
plt.plot(bins, chi2.pdf(bins, 9))   # カイ2乗分布（自由度9）を描画
