# -*- coding:utf-8 -*-

from pyhanlp import *
from ch03.msr import msr_dict, msr_train, msr_model, msr_test, msr_output, msr_gold


CWSEvaluator = SafeJClass('com.hankcs.hanlp.seg.common.CWSEvaluator')
FirstOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.FirstOrderHiddenMarkovModel')
SecondOrderHiddenMarkovModel = JClass('com.hankcs.hanlp.model.hmm.SecondOrderHiddenMarkovModel')
HMMSegmenter = JClass('com.hankcs.hanlp.model.hmm.HMMSegmenter')


def train(corpus, model):
    segmenter = HMMSegmenter(model)
    segmenter.train(corpus)
    print(segmenter.segment('商品和服务'))
    return segmenter.toSegment()


def evaluate(segment):
    result = CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict)
    print(result)


if __name__ == '__main__':
    segment = train(msr_train, FirstOrderHiddenMarkovModel())
    evaluate(segment)
    segment = train(msr_train, SecondOrderHiddenMarkovModel())
    evaluate(segment)
