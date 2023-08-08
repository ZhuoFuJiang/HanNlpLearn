# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 16:05
# @Author  : Zhuofu Jiang
# @FileName: speed_benchmark.py
# @Software: PyCharm


import time
from ch02.utility import load_dictionary
from ch02.forward_segment import forward_segment
from ch02.backward_segment import backward_segment
from ch02.bidirectional_segment import bidirectional_segment


def evaluate_speed(pressure, segment, text, dic):
    start_time = time.time()
    for i in range(pressure):
        segment(text, dic)
    elapsed_time = time.time() - start_time
    print("{} 万字/秒".format(len(text) * pressure / 10000 / elapsed_time))


if __name__ == "__main__":
    text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原"
    dic = load_dictionary()
    evaluate_speed(10000, forward_segment, text, dic)
    evaluate_speed(10000, backward_segment, text, dic)
    evaluate_speed(10000, bidirectional_segment, text, dic)
