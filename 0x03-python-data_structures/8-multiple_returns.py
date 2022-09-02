#!/usr/bin/python3
def multiple_returns(sentence):
    sent_len = len(sentence)
    if sent_len == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return ((sent_len, first_char))
