# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 13:26:48 2019

@author: u593120c

課題1-3:課題1-2と1-3の考え方で平方根を求める関数をそれぞれ作成し、スライド22枚目のようにmain関数を用いて、動作を確認するプログラムを作成せよ。また、他のプログラムからこのプログラムをモジュールとして用いて、各関数の動作を確認せよ。
"""

def k2(a, epsilon):
    x = 0.0
    numGuesses = 1

    if a < 1:
        min = a
        max = 1.0
        mem = [0, 0, 0]
        while abs(x ** 2 - a) >= epsilon:
            x = min + (max - min) / 2
            numGuesses += 1
            if (x ** 2 > a):
                max = x
            else:
                min = x
            if mem == [min, x, max]:
                break
            else:
                mem = [min, x, max]
    else:
        min = 1.0
        max = a
        mem = [0, 0, 0]
        while abs(x ** 2 - a) >= epsilon:
            x = min + (max - min) / 2
            numGuesses += 1
            if (x ** 2 > a):
                max = x
            else:
                min = x
            if mem == [min, x, max]:
                break
            else:
                mem = [min, x, max]

    # use flag for success confirmation
    # 成功の確認のためのブーリアン
    if abs(x**2 -a) >= epsilon:
        success = False
    else:
        success = True

    return success, x, numGuesses

def f(x,a):
    return x**2 - a

def fdev(x):
    return 2*x

def k3(a, epsilon):
    x = 1.0
    numGuesses = 1

    while abs(x ** 2 - a) >= epsilon:
        xnew = x - f(x, a) / fdev(x)
        if (x == xnew):
            break
        x = xnew
        numGuesses += 1

    if abs(x ** 2 - a) >= epsilon:
        success = False
    else:
        success = True

    return success, x, numGuesses


def main():
    import math

    a = float(input("Please input a positive number: "))

    s1,x1,n1 = k2(a, 0.01)
    if(s1):
        print(x1," is close to square root of ", a, "; took kadai1-2 ", n1, " guesses.")
    else:
        print("kadai1-2 failed on square root of ", a, "; took ", n1, " guesses. Closest guess: ", x1, " pow: ", x1 ** 2, " delta: ", abs(x1 ** 2 - a), " delta to math sqrt: ", abs(x1-math.sqrt(a)))

    s2,x2,n2 = k3(a, 0.01)
    if(s2):
        print(x2," is close to square root of ", a, "; took kadai1-3 ", n2, " guesses.")
    else:
        print("kadai1-3 failed on square root of ", a, "; took ", n2, " guesses. Closest guess: ", x2, " pow: ", x2 ** 2, " delta: ", abs(x2 ** 2 - a), " delta to math sqrt: ", abs(x2-math.sqrt(a)))


if __name__ == "__main__":
    main()