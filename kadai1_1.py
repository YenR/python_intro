# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:26:48 2019

@author: u593120c

課題1-1：a=0.25の場合も答えが求められるように変更せよ
"""

# change to positive numbers instead of integers
#　整数の代わりに、正数
a= float(input("Please input a positive number: "))

x= 0.0
epsilon = 0.01
step = epsilon**2
numGuesses = 1

# x=0.0からx**2とaの誤差がepsilon未満となるxを
# step=0.0001ごとに総当たりで調べる

# for numbers less than 1: go up to 1 instead of a
# 1未満の数なら、1へ上る
if a < 1:
    while abs(x**2-a)>=epsilon and x<1:
        x+= step
        numGuesses += 1
# unchanged
# 変更なし
else:
    while abs(x**2-a)>=epsilon and x<a:
        x+= step
        numGuesses += 1
    
print("numGuesses = ", numGuesses)  # 調べた回数
if abs(x**2 -a) >= epsilon:
    print("Failed on square root of ", a)
    #print("Closest guess: ", x, " pow: ", x**2, " delta: ", abs(x**2-a))
else:
    print(x," is close to square root of ", a)
    