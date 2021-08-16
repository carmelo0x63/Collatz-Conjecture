#!/usr/bin/env python3
# description: A Python function calculating Collatz conjecture's convergence
# author: Carmelo C
# email: carmelo.califano@gmail.com
# history (ISO 8601):
#   2021-08-16 - moved from CLI-tools
# source: https://en.wikipedia.org/wiki/Collatz_conjecture

def collatzSeq(n, outputSeq = None):
    if outputSeq is None:
        outputSeq = []
    outputSeq.append(int(n))
    while (n != 1):
        if (n % 2 == 0):
            return collatzSeq(n / 2, outputSeq)
        else:
            return collatzSeq(n * 3 + 1, outputSeq)
    return outputSeq

