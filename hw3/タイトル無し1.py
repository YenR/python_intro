# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:04:06 2019

@author: u593120c
"""


from scipy.stats import norm

param = [(0.0, 1.0), (-1.0, 6.0), (9.0, 9.0), (1.0, 0.5)]

for mean, std in param:
    print("mean: ", mean, ", std: ", std)
    for i in range(1,4):
        prob = norm.cdf(x=mean+i*std, loc=mean, scale=std) \
        -norm.cdf(x=mean-i*std, loc=mean, scale=std)
        print("-", i, "*std to ", i, "*std: ", prob)