# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 13:47:09 2019

@author: Tom Tucek トゥチェク・トム
"""

# 課題9:
# english_wordlist.txtを読み込み、回文（前から読んでも後ろから読んでも同じ語句）
# となる単語の個数を調べ、単語をリストアップせよ。


# check whether or not the given argument is a palindrome, returning True if it is
def check_palindrome(word):
    l = len(word)
    # iterate through the word
    for i in range(l):
        # if half was passed, stop
        if i >= int(l/2):
            break
        # if current letter and corresponding one at the other and do not match up -> not a palindrome
        if word[i] != word[l-i-1]:
            return False
    # if no problem found -> palindrome
    return True


if __name__ == "__main__":
    # counter for number of palindromes
    cnt = 0
    # open file
    with open('english_wordlist.txt') as f:
        # read every word
        for line in f:
            # remove white spaces
            line = line.strip()
            # check if the word is a palindrome, if so, print it out and increase counter
            if check_palindrome(line):
                print(line)
                cnt += 1
    # print out number of found palindromes
    print("Number of palindromes found: " + str(cnt))
