# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:07:12 2019

@author: Tom Tucek トゥチェク・トム
"""

# 課題2:リスト中の値の平均，分散，標準偏差を求める関数を作成し，
# randomで生成したN個の整数からなるリストに適用せよ．
# ※random以外のモジュールは使用しないこと
# ※標準偏差を求めるとき、squareroot.py（1回目資料の２１枚目のスライド参照）を利用せよ

import random
import statistics

# number of elements, bounds for randomly generated numbers
N = 25
ran_min = -100
ran_max =  100

# squareroot.pyから
def get_squareroot(a):
    x= 0.0
    epsilon = 0.01
    step = epsilon**2

    while abs(x**2-a)>=epsilon and x<a:
        x+= step
    if abs(x**2 -a) >= epsilon:
        print("Failed on square root of ", a)
    else:
        return x

# formula: mean = sum of all elements / number of elements
def mean(list):
    return sum(list) / len(list)


# formula: var = sum((xi - mean(x))^2) / n
def var(list):
    m = mean(list)
    sum = 0.0

    for x in list:
        sum += (x - m)**2

    return sum / (len(list))


# standard deviation = square root of variance
def stddev(list):

    return get_squareroot(var(list))
        

def main():
        
    List = []
    # fill list with N random values in range from ran_min to ran_max
    for i in range(0, N, 1):
        List.append(random.uniform(ran_min, ran_max))

    print('List with N=' + str(len(List)) + ' Elements:')
    print(List)
    print('\nMean:')
    print(mean(List))
    print(statistics.mean(List))

    print('\nVariance:')
    print(var(List))
    print(statistics.pvariance(List))

    print('\nStandard deviation:')
    print(stddev(List))
    print(statistics.stdev(List))

    
if __name__ == "__main__":   
    main()