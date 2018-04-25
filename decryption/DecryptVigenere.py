#!/usr/bin/env python

import sys
import boto3
from botocore import exceptions
from etao440 import VigenereCipher, NgramFrequencyScorer
from etao440.freq import ENGLISH_DIGRAMS, ENGLISH_FREQ
from Frequency import lang_di, lang_freq


def lambda_handler(text, language="en"):
    """
    Invoked by Lambda

    :param event: contains the S3 bucket and key for the OCR file to be decrypted
    :param context: metadata associated with this Lambda/Step Function execution
    :return: a dictionary passed back to Lambda containing the input data, decrypted text, and confidence
    """

    scorer = NgramFrequencyScorer(freq=lang_di(language))

    highest = {
        "confidence": 0.0,
        "text": ""
    }

    for key in keys([chr(x) for x in range(ord('A'), ord('C') + 1)], 4):
        vc = VigenereCipher(key)
        decrypted = vc.decrypt(text)
        result = (scorer.score(decrypted), decrypted)
        if result[0] > highest["confidence"]:
            highest["confidence"] = result[0]
            highest["text"] = result[1]

    return highest


def keys(chars, num, prev=""):
    """
    Generates decryption keys
    :param chars: the characters to include in the key
    :param num: the max length of the key
    :return: keys
    """
    for c in map(ord, chars):
        if num == 1:
            yield "".join([chr(c), prev])
        else:
            for k in keys(chars, num - 1, "".join([chr(c), prev])):
                yield k