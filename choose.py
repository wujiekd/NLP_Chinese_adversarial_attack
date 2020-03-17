
import random
import jieba
import json
import numpy as np



# 加载用户自己的模块
from Pinyin2Hanzi import DefaultDagParams
from Pinyin2Hanzi import dag
import fasttext
from pypinyin import lazy_pinyin
import re
from jieba.analyse import *
from distance_module import *
distance = DistanceCalculator()

f1 = open("./raw.txt","r")
lines = f1.readlines()
REGEX_TO_REMOVE = re.compile(r"[^\u4E00-\u9FA5]")
dagParams = DefaultDagParams()
model = fasttext.load_model('reference_model/mini-explicit-labels.ftz')

raw_word = [line.replace("\n","") for line in lines]

change_word = raw_word

alpha = 1
beta = 1

for i in range(len(raw_word)):
    ch = raw_word[i]
    chacha = model.predict(ch, k=2)
    if (chacha[0][0] == '__label__辱骂'):
        P1 = chacha[1][0]
    else:
        P1 = chacha[1][1]
    pinyin = lazy_pinyin(ch)
    max_point= 0
    change_ch=ch
    result = dag(dagParams, pinyin, path_num=5, log=True)
    for j in range(5):
        if len(result)>j:
            ss = ""
            for c in result[j].path:
                ss = c
            chacha =model.predict(ss, k=2)
            if (chacha[0][0] == '__label__辱骂'):
                P2 = chacha[1][0]
            else:
                P2 = chacha[1][1]
            if ss == ch :continue
            four_dis = distance([ch], [ss])
            all_dis =3.0 / 14 * (1 - four_dis['normalized_levenshtein'][0]) + 1.0 / 7 * (1 - four_dis['jaccard_word'][0]) + 3.0 / 14 * (
            1 - four_dis['jaccard_char'][0]) + 3.0 / 7 * (1 - four_dis['embedding_cosine'][0])

            """
            Our core formula
            """
            point = (P1 - P2)**alpha + all_dis**beta


            if max_point < point:
                change_ch=ss
                max_point =point
    change_word[i]=change_ch

changeword_s = [line.replace("\n","") for line in change_word]
print(changeword_s)

out=open("./change.txt",'w')
lists = [sentence + "\n"  for sentence in changeword_s]
out.writelines(lists)