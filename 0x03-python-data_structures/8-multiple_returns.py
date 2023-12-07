#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        len_sentce = len(sentence)
    else:
        len_sentce = 0
    return (len_sentce, sentence if not sentence else sentence[:1])
