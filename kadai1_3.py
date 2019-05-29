# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:26:48 2019

@author: u593120c

課題1-3:下記のようにニュートン法（※)で探索するように変更し、調べた回数を変更前と比較せよ。
"""

a= float(input("Please input a positive number: "))

x= 1.0
epsilon = 0.01
numGuesses = 1

# f(x) = x²-a=0 implementation / 実装
def f(x,a):
    return x**2 - a

# f'(x) = 2x=0 implementation / 実装
def fdev(x):
    return 2*x

while abs(x**2-a)>=epsilon:
    xnew = x -f(x,a)/fdev(x)
    if(x==xnew):
        break
    x=xnew
    #print("x: ", x)
    numGuesses += 1
    
print("numGuesses = ", numGuesses)  # 調べた回数
if abs(x**2 -a) >= epsilon:
    print("Failed on square root of ", a)
    print("Closest guess: ", x, " pow: ", x**2, " delta: ", abs(x**2-a))
else:
    print(x," is close to square root of ", a)
    