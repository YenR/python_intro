# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:09:15 2019

@author: Tom Tucek トゥチェク・トム
"""
import random

UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = UPPER.lower()
SYMBOL = "!?,. ;*'"
LETTERS = UPPER+LOWER+SYMBOL
NUMBERS = '0123456789,'

def check(message, mode):
    if mode==0:
        diff = set(list(message)) - set(LETTERS)
        if diff:
            return 0, diff
    elif mode==1:
        diff = set(list(message)) - set(NUMBERS)
        if diff:
           return 0, diff
    return 1, diff

def change_mode(mode, to_mode, encoded):
    while (mode!=to_mode):
        encoded += ',' + str(27*random.randint(0,100))
        mode = (mode+1) % 3
    return mode, encoded

def encode(message):
    mode = 0
    encoded = ''
    for l in message:
        if l in UPPER:
            mode, encoded = change_mode(mode, 0, encoded)
            encoded += ','+str(27*random.randint(0,100)+UPPER.find(l)+1)
        elif l in LOWER:
            mode, encoded = change_mode(mode, 1, encoded)
            encoded += ','+str(27*random.randint(0,100)+LOWER.find(l)+1)
        else:
            mode, encoded = change_mode(mode, 2, encoded)
            encoded += ','+str(9*random.randint(0,100)+SYMBOL.find(l)+1)
    encoded = encoded.lstrip(',')
    return encoded

def decode(message):
    mode = 0
    decoded = ''
    num_list= [int(x) for x in message.split(',')]
    for num in num_list:
        if mode==0:
            if num%27==0:
                mode = 1
            else: 
                decoded += UPPER[num%27-1]
        elif mode==1:
            if num%27==0:
                mode = 2
            else:
                decoded += LOWER[num%27-1]
        else:
            if num%9==0:
                mode = 0
            else: 
                decoded += SYMBOL[num%9-1]
    return decoded


if __name__=="__main__":
    Mode = int(input("Press 0 for encode, 1 for decode: "))
    if Mode==0 or Mode==1:
        message = input("Input a message¥n")
        valid, diff = check(message, Mode) #messageがModeと合っているか確認
        if valid:
            if Mode==0:
                encoded = encode(message) 
                print("encoded message: ", encoded)
            else:
                decoded = decode(message) 
                print("decoded message: ", decoded)
        else:
            print("your message contains illegal letters: ", ', '.join(diff))
    else:
        print("Illegal option")
        
        