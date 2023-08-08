# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 15:49
# @Author  : Zhuofu Jiang
# @FileName: forward_segment.py
# @Software: PyCharm


from ch02.utility import load_dictionary


def forward_segment(text, dic):
    word_list = []
    i = 0
    while i < len(text):
        longest_word = text[i]
        for j in range(i+1, len(text) + 1):
            word = text[i: j]
            if word in dic:
                if len(word) > len(longest_word):
                    longest_word = word
        word_list.append(longest_word)
        i += len(longest_word)
    return word_list


if __name__ == "__main__":
    dic = load_dictionary()
    print(forward_segment("研究生命起源", dic))
