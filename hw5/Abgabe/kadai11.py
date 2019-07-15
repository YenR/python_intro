# -*- coding: utf-8 -*-
"""

@author: Tom Tucek トゥチェク・トム
"""

# using regex
import re
import random
import time
from collections import Counter

# 課題11-9:
# ciはj=a * i+b (modN) で算出されるcjで置き換えられるため、ciとcjの対が2対あれば、a、bが求められる。
# そこで、英文における文字の頻度の偏りを利用してciとcjの対を2対推測する。
# 例えば、一般的に英文で最も使われる文字は’e’、最も使われない文字は’z’とする。
# このとき、暗号文において最も使われている文字、使われていない文字をそれぞれ’e’、’z’に対するcjと推測する。
# このように頻度に基づき、a,bの候補を限定した上で、課題10-8と同様に、暗号化の際に用いられたと推定される
# 鍵a,b、及び解読結果を出力するプログラムを作成せよ。
# ただし、一般的な英文での文字の頻度（※）と暗号文における文字の頻度に基づき、
# 2対のciとcjの候補を決定する関数、及び、2対のciとcjからa,bを求める関数を作成して用いよ。

# 課題11-10:
# enc_wa.txtを読み込み、課題11-8、課題11-9で作成したプログラムにより、鍵及び元の平文を推定せよ。
# 候補となった鍵対の数、及び解読にかかった時間を比較せよ。
# ※timeモジュールを用いてimport timetime.time()で現在時刻（ある起点からの経過時間）が取得できる。

# 課題11-11:
# 適当な平文をa,b=(1,0)、a>=N、b>=N、Nと互いに素でないaなどの鍵で暗号化した後、
# 必要であれば、課題11-6で作成したプログラムを用いて、鍵を用いて暗号文を解読したり、
# 課題11-10で作成したプログラムを用いて鍵及び元の平文を推定し、どのような問題が生じるか考察せよ。


UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = UPPER.lower()
SYMBOL = " -!\"&'()*,.:;[]_`?\n"
NUMBERS = '0123456789'
COMP = UPPER + LOWER + NUMBERS + SYMBOL
N = len(COMP)

# depth of character frequency array -> time scales exponentially to DEPTH so careful.
# 5 works for most examples, 4 does not work for enc_wa.txt
DEPTH = 5
# threshold in percent for text to be added into collection
# eg text has to be at least 20% English to be considered a successful result
THRESHOLD = 0.2

# check if contents of message conform to character set defined by COMP
def check(message):
    # set of differing characters
    diff = set(list(message)) - set(COMP)
    if diff:
        return 0, diff
    return 1, diff


# 課題11-3:
# 2つの鍵とテキストが与えられたとき、
# アフィン暗号による暗号文を返す関数を作成せよ。
# encode a message using affine cipher
def encode(message, a, b):
    encoded = ''
    # iterate through every character of the message
    for c in message:
        # find usual position in character set
        i = COMP.find(c)
        # perform affine cipher transformation
        i = (i * a + b) % N
        # save encoded characters in new string and return it
        encoded += COMP[i]
    return encoded


# decode a message using affine cipher
def decode(message, a, b):
    decoded = ''
    x = euclid_extended(a,N)
    if x == "a is not invertible":
        return -1
    # iterate through every character of the message
    for c in message:
        # find usual position in character set
        i = COMP.find(c)
        # when decoding, shift back instead of ahead
        i = (x * (i - b)) % N
        # save decoded characters in new string and return it
        decoded += COMP[i]
    return decoded


# 課題11-1:
# ユークリッドの互除法（※）を利用して、
# xとyの最大公約数gcd x,yを求める関数を作成せよ。
def euclid_gcd(a,b):
    while b != 0:
        t = b
        b = a%b
        a = t
    return a


# 課題11-2:
# 課題11-1で作成した関数とモジュールrandomを用いて、
# アフィン暗号の条件を満たすような2つの鍵keyA=a、keyB=bを生成する関数を作成せよ。
def create_keys():
    a = random.randint(2, N-1)
    b = random.randint(1, N-1)
    
    while euclid_gcd(a,N) != 1:
        a = random.randint(2, N-1)
        
    return a,b
    

# 課題11-4:
# 文字集合Cに属する文字に構成される任意のテキストをテキストファイル（例：plaintext.txt）に保存せよ。
# このテキストファイルを読み込み、課題11-2で作成した2つの鍵を用いて暗号化し、
# 暗号文を別のテキストファイルに保存するプログラムを作成せよ。
def encrypt_file(filename):
    a,b = create_keys()
    
    with open(filename) as f:
        txt = f.read()
        
        valid, diff = check(txt)
        if valid:
            
            encoded = encode(txt, a, b)
            f2 = open("enc_" + filename, "w")
            f2.write(encoded)
            f2.close()
            
            f2 = open("keys_enc_" + filename, "w")
            f2.write(str(a) + "\n")
            f2.write(str(b) + "\n")
            f2.close()
            
            return True
        else:
            print("Error: read file '" + filename + "' contains illegal characters: ", ', '.join(diff))
            return False

    
# 課題11-5:
# 拡張ユークリッドの互除法（※）を利用して、aとNが与えられたとき、
# ax=1(modN)となるxを求める関数を作成せよ。
# taken from: https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
def euclid_extended(a, n):
    t = 0
    newt = 1
    r = n
    newr = a
    
    while newr != 0:
        quotient = int(r / newr)
        r, newr = newr, r - quotient * newr
        t, newt = newt, t - quotient * newt
        
    if r > 1: 
        return "a is not invertible"
    if t < 0:
        t = t + n
    
    return t


# 課題11-6:
# 課題11-4で作成した暗号文と暗号化に用いた2つの鍵が与えられたとき、
# 課題11-5で作成した関数を用いて、暗号文を解読した結果を出力するプログラムを作成せよ
# （課題11-4で暗号文を保存した後に追記し、解読文が平文と等しいか確認すればよい）。
def decrypt_file(filename):    
    with open("keys_" + filename) as f:
        a = int(f.readline())
        b = int(f.readline())
        
    with open(filename) as f:
        decoded = f.read()        
        txt = decode(decoded, a, b)
    
    return txt
    

# 課題11-7:
# あるテキストが与えられたとき、文中に含まれる英単語の割合を算出する関数を作成せよ。
# ただし英単語のリストはenglish_wordlist.txtから得てよい。
# また、できるだけ正しく英単語の割合が算出できるよう、テキストに対してはアルファベットのみから
# 構成される単語を抽出するといった前処理を施すこと。

# returns a percentage (0~1) of how much of the given texts words are part of the given dictionary
def english_percentage(dictionary, text):
    res = re.findall(r'\w+', text)
    #res = re.split(r"[\s\.,\?]+",text)
    #res = text.split()

    hits = 0
    total = 0

    for element in res:
        if len(element) > 1:
            if element.lower() in dictionary:
                hits += 1
            total += 1

    return hits / total


# 課題11-8:
# 暗号文のみが与えられたとき、有り得るすべての鍵a,bを用いて課題11-6と同様に暗号文を解読する。
# 各鍵対に対して出力される解読文に対し、課題11-7で作成した関数を用いて、含まれる英単語の割合を算出し、
# それに基づき、暗号化の際に用いられたと推定される鍵a,b及び解読結果を出力するプログラムを作成せよ。
def decrypt_brute_force(text, dictionary):

    collection = []
    count_candidates = 0    # number of candidates for key pairs = number of cycles

    for a in range(2, N):
        if euclid_gcd(a, N) == 1:
            for b in range(1,N):
                count_candidates +=1
                result = decode(text, a, b)
                percent = english_percentage(dictionary, result)
                if percent > THRESHOLD:
                    collection.append((percent, result, a, b))
        #print(a, collection)

    max = THRESHOLD
    result = (0,0,0,0)
    for (p, r, a, b) in collection:
        if p > max:
            max = p
            result = r,a,b, count_candidates

    return result

# returns n most frequent and n least frequent characters in text
def frequent_characters(text, n):
    ct = Counter(text)
    top = ct.most_common(n)
    top = [x[0] for x in top]

    bottom = ct.most_common()[:-n-1:-1]
    bottom = [x[0] for x in bottom]

    return top, bottom


def solve_for_ab(i1, j1, i2, j2):
    # from
    #  j1 = a * i1 + b mod N
    #  j2 = a * i2 + b mod N
    # leads to
    #  (i1-i2)b = j2i1-j1i2 mod N
    #  (i2-i1)a = j2-j1 mod N

    # solve for b
    # (i1-i2)b = j2i1-j1i2 mod N
    # -> x*b = y mod N
    x = i1 - i2
    y = j2 * i1 - j1 * i2
    # solve by multiplying with t so that x*t mod N = 1
    # -> b = y * t mod N
    t = euclid_extended(x,N)
    if t == "a is not invertible":
        return 0,0
    b = (y * t) % N

    # solve for a
    # (i2-i1)a = j2-j1 mod N
    # -> x*a = y mod N
    x = i2 - i1
    y = j2 - j1
    # same as above, multiply both sides with multiplicative inverse of x,N
    t = euclid_extended(x,N)
    if t == "a is not invertible":
        return 0,0
    a = (y * t) % N

    return a, b

# decrypts given text using character frequency analysis
# dic is the used dictionary to check for english results
# n is the number of characters taken for testing purposes
def decrypt_frequency_analysis(txt, dic, n):
    # use random english text as example for character frequencies (http://www.randomtextgenerator.com/)
    with open('english_randomtext.txt') as f:
        txt2 = f.read()
    top, bottom = frequent_characters(txt2, n)
    enc_top, enc_bottom = frequent_characters(txt, n)

    collection = []

    ## old code which used rarest characters. did not work well
    # for x in range(0, n):
    #     for y in range(0, n):
    #         i1 = COMP.find(top[x])
    #         i2 = COMP.find(bottom[x])
    #         j1 = COMP.find(enc_top[y])
    #         j2 = COMP.find(enc_bottom[y])
    #
    #         a,b = solve_for_ab(i1,j1,i2,j2)
    #         dec = decode(txt, a, b)
    #
    #         if dec != -1 :
    #             percent = english_percentage(dic, dec)
    #             if percent > 0.2:
    #                 texts.append((percent, dec, a, b))

    iList = [COMP.find(i) for i in top]
    jList = [COMP.find(j) for j in enc_top]
    count_candidates = 0    # number of candidates for key pairs = number of cycles

    for x in range(0, len(iList)):
        for xx in range(x+1, len(iList)):
            for y in range(0, len(jList)):
                for yy in range(y+1, len(jList)):
                    count_candidates += 1
                    i1 = iList[x]
                    i2 = iList[xx]
                    j1 = jList[y]
                    j2 = jList[yy]

                    a,b = solve_for_ab(i1,j1,i2,j2)
                    dec = decode(txt, a, b)

                    if dec != -1 :
                        percent = english_percentage(dic, dec)
                        if percent > THRESHOLD:
                            collection.append((percent, dec, a, b))

    result = (0,0,0,0)
    max = THRESHOLD
    for (p, r, a, b) in collection:
        if p > max:
            max = p
            result = r, a, b, count_candidates

    return result


# fill dictionary with english words from wordlist file
def getDictionary():
    dic = []
    with open('english_wordlist.txt') as f:
        # read every word
        for line in f:
            # remove white spaces
            line = line.strip()
            dic.append(line)
    return dic


if __name__ == "__main__":
    
    encrypt_file('example_text.txt')
    txt = decrypt_file('enc_example_text.txt')
    print(txt)

    dic = getDictionary()
    with open('enc_wa.txt') as f:
        txt = f.read()

    #
    # -- Brute Force Method ---
    #
    start = time.time()
    br, ba, bb, bc = decrypt_brute_force(txt, dic)
    end = time.time()
    brute_force_timer = end-start

    if br:
        print("Brute Force method successful.")
        print("--Result:--\n", br, "--End Result--")
        print("Keys found:", ba, bb)
        print("Number of key candidates:", bc)
        print("Time needed:", brute_force_timer, "s")
    else:
        print("Brute Force method unsuccessful.")
        print("Time needed:", brute_force_timer, "s")

    #
    # --  Character Frequency Analysis --
    #
    start = time.time()
    cr, ca, cb, cc = decrypt_frequency_analysis(txt, dic, DEPTH)
    end = time.time()
    frequency_analysis_timer = end-start

    print("\n---\n")
    if cr:
        print("Character Frequency Analysis successful.")
        print("--Result:--\n", cr, "--End Result--")
        print("Keys found:", ca, cb)
        print("Number of key candidates:", cc)
        print("Time needed:", frequency_analysis_timer, "s")
    else:
        print("Character Frequency Analysis unsuccessful.")
        print("Time needed:", frequency_analysis_timer, "s")