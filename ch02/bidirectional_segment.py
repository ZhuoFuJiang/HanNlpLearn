# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 16:00
# @Author  : Zhuofu Jiang
# @FileName: bidirectional_segment.py
# @Software: PyCharm


from ch02.utility import load_dictionary
from ch02.forward_segment import forward_segment
from ch02.backward_segment import backward_segment


def count_single_char(word_list):
    return sum(1 for word in word_list if len(word) == 1)


def bidirectional_segment(text, dic):
    f = forward_segment(text, dic)
    b = backward_segment(text, dic)
    if len(f) < len(b):
        return f
    elif len(f) > len(b):
        return b
    else:
        if count_single_char(f) < count_single_char(b):
            return f
        else:
            return b


if __name__ == "__main__":
    dic = load_dictionary()
    print(bidirectional_segment("结婚的和尚未结婚的", dic))
