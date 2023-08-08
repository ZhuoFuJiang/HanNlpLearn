# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 15:46
# @Author  : Zhuofu Jiang
# @FileName: fully_segment.py
# @Software: PyCharm


from ch02.utility import load_dictionary


def fully_segment(text, dic):
    word_list = []
    for i in range(len(text)):
        for j in range(i+1, len(text) + 1):
            word = text[i: j]
            if word in dic:
                word_list.append(word)
    return word_list


if __name__ == "__main__":
    dic = load_dictionary()
    print(fully_segment("商品和服务", dic))
