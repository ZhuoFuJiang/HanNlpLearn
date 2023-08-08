# -*- coding: utf-8 -*-
# @Time    : 2023/7/14 15:41
# @Author  : Zhuofu Jiang
# @FileName: utility.py
# @Software: PyCharm


from pyhanlp import *


def load_dictionary():
    """
    加载HanLP中的mini词库
    :return: 一个set形式的词库
    """
    IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')
    path = HanLP.Config.CoreDictionaryPath.replace('.txt', '.mini.txt')
    dic = IOUtil.loadDictionary([path])
    return set(dic.keySet())


if __name__ == '__main__':
    dic = load_dictionary()
    print(len(dic))
    print(list(dic)[0])