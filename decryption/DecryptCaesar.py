#!/usr/bin/env python

from etao440 import CaesarCipher
from etao440.scorers import NgramFrequencyScorer
from decryption.Frequency import lang_di, SPANISH_DIGRAMS, FRENCH_DIGRAMS


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

    for n in range(25):
        decrypted = CaesarCipher(n).decrypt(text)
        score = scorer.score(decrypted)
        if score > highest["confidence"]:
            highest["confidence"] = score
            highest["text"] = decrypted

    return highest

