# -*- coding: utf-8 -*-
"""
Created on Fri May 17 13:04:06 2019

@author: u593120c
"""

import random
import matplotlib.pyplot as plt

# N = number of cards, probes = number of repeated simulations
N = 100
probes = 1000

# runs the defined game, returns True if won and False if lost
def simulate(cards, m):
    highest = 0

    for i in range(0, m):
        if cards[i] > highest:
            highest = cards[i]

    changes = 0

    for i in range(m, len(cards)):
        if cards[i] > highest:
            highest = cards[i]
            changes += 1

    if changes == 1:
        return True
    else:
        return False


def main():
    # 課題8: 1～Nまでの番号が付いたカードを裏返して並べる。
    # この中から最大の番号が付いたものを選びたい。
    # 左端から順番に表向け、M枚までの最大値を閾値とし、M枚目以降に閾値を超える最初のカードを選んだとき、
    # それが最大値であればあなたの勝ちである。
    # Mをどう設定すれば勝率が最大となるか、シミュレーションにより決定せよ。
    # また、横軸をM（もしくはM/N）、縦軸を勝つ確率としたグラフをプロットせよ。

    # create deck with N cards
    cards = []
    for i in range(1, N + 1):
        cards.append(i)

    # save success rate for each m
    success = [0] * N

    # simulate a defined number of times, each time with a newly shuffled deck of cards
    for i in range(0, probes):

        random.shuffle(cards)

        # simulate for every number from 1 to N-1 and save success flag in list
        for m in range(1, N):
            if simulate(cards, m):
                success[m] += 1

    # convert success list to percentages
    success = [(x/probes) * 100 for x in success]

    print("Highest winning percentage at: " + str(success.index(max(success))) + "/" + str(N) + " with " + str(max(success)) + "%")

    # plot success rate
    plt.plot(success)
    plt.xlabel('M',fontsize=12)
    plt.ylabel('Winning percentage',fontsize=12)
    plt.ylim(0, 100)
    plt.title('Simulation of job hunting problem, N=' + str(N) + ', repetitions=' + str(probes),fontsize=14)
    plt.show()


if __name__ == "__main__":
    main()