# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:07:12 2019

@author: u593120c
"""

# 課題3-1:
# 地球上の2地点（2対の緯度経度）
# 間の距離を算出する関数を作成せよ。
# ※モジュールmathを使用せよ。

import math
import pandas as pd

# radius of the earth in km
r = 6378.1


def hav(theta):
    return math.sin(theta / 2) ** 2


def distance(p1, p2):
    return r * 2 * math.asin(math.sqrt(hav(p2[0]-p1[0]) + math.cos(p1[0]) * math.cos(p2[0]) * hav(p2[1] - p1[1])))


def main():

    loc_df = pd.read_csv('locations.csv')
    loc_dict = loc_df.set_index('name').T.apply(tuple).to_dict()

    # convert from degrees to radians (waste of resources)
    # for k in loc_dict:
    #    loc_dict[k] = (math.radians(loc_dict[k][0]), math.radians(loc_dict[k][1]))

    print("from: ", end = '')
    i1 = input()
    if i1 not in loc_dict:
        print("Error: Could not find " + i1)
        return

    print("to: ", end = '')
    i2 = input()
    if i2 not in loc_dict:
        print("Error: Could not find " + i2)
        return

    print("distance: " + str(distance((math.radians(loc_dict[i1][0]), math.radians(loc_dict[i1][1])), (math.radians(loc_dict[i2][0]), math.radians(loc_dict[i2][1])))) + " km")


if __name__ == "__main__":   
    main()