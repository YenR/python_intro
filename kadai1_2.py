# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:26:48 2019

@author: u593120c

課題1-2:下記のように2分法で探索するように変更し、調べた回数を変更前と比較せよ
"""

a= float(input("Please input a positive number: "))

x= 0.0
epsilon = 0.01
numGuesses = 1

# if less than 1, start in range a to 1, otherwise 1 to a
# aは1未満なら、a～1で始め、さもないと1～aで始める
if a < 1:
    min=a
    max=1.0
    mem = [0, 0, 0]
    while abs(x**2-a)>=epsilon:
        x=min + (max-min)/2
        #print("x: ", x, ", min: ", min, ", max: ", max)
        numGuesses += 1
        if(x**2 > a):
            max=x
        else:
            min=x
        if mem == [min, x, max]:
            break
        else:
            mem = [min, x, max]
            #print(mem)

# example edge case: 125678765432345678987654, memory needed to prevent infinite loop
# a = 125678765432345678987654　などは例外で、普通にループは終了しないので、記憶のための変数を使用（mem）
else:
    min=1.0
    max=a
    mem=[0,0,0]
    while abs(x**2-a)>=epsilon:
        x=min + (max-min)/2
        #print("x: ", x, ", min: ", min, ", max: ", max)
        numGuesses += 1
        if(x**2 > a):
            max=x
        else:
            min=x
        if mem == [min,x,max]:
            break
        else:
            mem=[min,x,max]
            #print(mem)

    
print("numGuesses = ", numGuesses)  # 調べた回数
if abs(x**2 -a) >= epsilon:
    print("Failed on square root of ", a)
    print("Closest guess: ", x, " pow: ", x**2, " delta: ", abs(x**2-a))
else:
    print(x," is close to square root of ", a)
    