# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:09:15 2019

@author: Tom Tucek トゥチェク・トム
"""
import random

UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = UPPER.lower()
SYMBOL = " -!\"&'()*,.:;[]_`?\n"
NUMBERS = '0123456789'
COMP = UPPER + LOWER + NUMBERS + SYMBOL
N = len(COMP)

# 課題10-1：
# 文字集合cを、アルファベット大文字小文字、数字、記号とする。
# 鍵をランダムに生成し、与えられたテキストをシーザー暗号により暗号化するプログラムを作成せよ。
# また、暗号文を生成時の鍵を用いて解読し、元のテキストと同じか確認せよ。
# ※解読には𝑐𝑗をどのような𝑐𝑖に置き換えればよいか考えよ。


# check if contents of message conform to character set defined by COMP
def check(message):
    # set of differing characters
    diff = set(list(message)) - set(COMP)
    if diff:
        return 0, diff
    return 1, diff


# encode a message using caesar shift
def encode(message, cipher):
    encoded = ''
    # iterate through every character of the message
    for c in message:
        # find usual position in character set
        i = COMP.find(c)
        # shift position by number of positions defined by cipher parameter
        i = (i+cipher) % N
        # save encoded characters in new string and return it
        encoded += COMP[i]
    return encoded


# decode a message using caesar shift
def decode(message, cipher):
    decoded = ''
    # iterate through every character of the message
    for c in message:
        # find usual position in character set
        i = COMP.find(c)
        # when decoding, shift bach instead of ahead
        i = (i - cipher) % N
        # save decoded characters in new string and return it
        decoded += COMP[i]
    return decoded


if __name__ == "__main__":
    Mode = int(input("Press 0 for encode, 1 for decode: "))
    if Mode == 0 or Mode == 1:
        message = input("Please input a message: ")
        # check if characters in message are valid
        valid, diff = check(message)
        if valid:
            if Mode == 0:
                # use random cipher for encoding
                cipher = random.randint(1, N-1)
                # encode message
                encoded = encode(message, cipher)
                # print it together with cipher needed for decoding
                print("Encoded message using cipher [" + str(cipher) + "]: ", encoded)
            else:
                # use input cipher for decoding
                cipher = int(input("Please input the cipher: "))
                # decode message
                decoded = decode(message, cipher)
                # print it
                print("Decoded message using cipher [" + str(cipher) + "]: ", decoded)
        else:
            print("Your message contains illegal letters: ", ', '.join(diff))
    else:
        print("Illegal option")
