# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 15:54
# @Author  : Zhuofu Jiang
# @FileName: backward_segment.py
# @Software: PyCharm


from ch02.utility import load_dictionary


def backward_segment(text, dic):
    word_list = []
    i = len(text) - 1
    while i >= 0:
        longest_word = text[i]
        for j in range(0, i):
            word = text[j: i+1]
            if word in dic:
                if len(word) > len(longest_word):
                    longest_word = word
        word_list.insert(0, longest_word)
        i -= len(longest_word)
    return word_list


if __name__ == "__main__":
    dic = load_dictionary()
    print(backward_segment("研究生命起源", dic))