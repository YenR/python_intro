# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 13:29:09 2019

@author: u593120c
"""

import csv

m_height = []     # 空のリストを作成
m_weight = []
f_height = []
f_weight = []

with open('weight-height.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # ヘッダーの読み飛ばし
    for row in reader:
        if row[0]=='Male':
            m_height.append(float(row[1]))  # リストに追加
            m_weight.append(float(row[2]))
        elif row[0]=='Female':
            f_height.append(float(row[1]))
            f_weight.append(float(row[2]))
            
            
#print(m_height)            
            
            
import pandas as pd
data = pd.read_csv('weight-height.csv')
