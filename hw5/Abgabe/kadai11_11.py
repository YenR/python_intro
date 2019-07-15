# -*- coding: utf-8 -*-
"""

@author: Tom Tucek トゥチェク・トム
"""

import kadai11
import random

# 課題11-11:
# 適当な平文をa,b=(1,0)、a>=N、b>=N、Nと互いに素でないaなどの鍵で暗号化した後、
# 必要であれば、課題11-6で作成したプログラムを用いて、鍵を用いて暗号文を解読したり、
# 課題11-10で作成したプログラムを用いて鍵及び元の平文を推定し、どのような問題が生じるか考察せよ。
if __name__ == "__main__":

    with open('example_text.txt') as f:
        text = f.read()
    dic = kadai11.getDictionary()

    a,b = 1,0
    encoded = kadai11.encode(text, a, b)
    decoded = kadai11.decode(encoded, a, b)
    cracked,_,_,_ = kadai11.decrypt_frequency_analysis(encoded, dic, kadai11.DEPTH)
    print("a,b = 1,0 decryption using keys, Success:", decoded == text)
    print("a,b = 1,0 decryption character frequency analysis, Success:", cracked == text)

    print("---")

    x, y = random.randint(1,10), random.randint(1,10)
    a, b = kadai11.N+x, kadai11.N+y
    encoded = kadai11.encode(text, a, b)
    decoded = kadai11.decode(encoded, a, b)
    cracked,_,_,_ = kadai11.decrypt_frequency_analysis(encoded, dic, kadai11.DEPTH)
    print("a,b = N+" + str(x) + ",N+" + str(y) + " decryption using keys, Success:", decoded == text)
    print("a,b = N+" + str(x) + ",N+" + str(y) + " decryption character frequency analysis, Success:", cracked == text)

    print("---")

    a, b = int(kadai11.N/3), 1
    encoded = kadai11.encode(text, a, b)
    decoded = kadai11.decode(encoded, a, b)
    cracked,_,_,_ = kadai11.decrypt_frequency_analysis(encoded, dic, kadai11.DEPTH)
    print("a,b = N/3,1 decryption using keys, Success:", decoded == text)
    print("a,b = N/3,1 decryption character frequency analysis, Success:", cracked == text)

    print("\n\n--Encoded result--\n", encoded)

