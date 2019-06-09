# -*- coding: utf-8 -*-
"""

@author: Tom Tucek トゥチェク・トム
"""
import kadai10_1

# 課題10-2：
# enc_wc.txtを読み込み、有り得るすべての鍵を用いて解読したテキストを見て、
# 生成時の鍵、及び元のテキストを推定せよ。


if __name__ == "__main__":
    # open file
    with open('enc_wc.txt') as f:
        # read entire file content
        txt = f.read()
        # gather decoded text in string
        collection = ""
        # iterate through all possible keys
        for i in range(1, kadai10_1.N):
            # decipher with current key
            dec = kadai10_1.decode(txt, i)
            # save decoded text
            collection += ("\n---\nDecoded text using cipher [" + str(i) + "]:\n---\n" + dec)

    # write result into another file (overwrites previous contents)
    f2 = open("dec_wc.txt", "w")
    f2.write(collection)
    f2.close()

    # or print it out
    # print(collection)


