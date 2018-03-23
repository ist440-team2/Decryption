#!/usr/bin/env python

from etao import CaesarCipher, NgramFrequencyScorer
from etao.freq import ENGLISH_DIGRAMS


def lambda_handler(event, context):
    """
    Invoked by Lambda

    :param event: input data passed in by Step Function
    :param context: metadata associated with this Lambda/Step Function execution
    :return: a dictionary passed back to Lambda containing the input data, decrypted text, and confidence
    """
    output = {}
    text = str(event["inputText"])

    scorer = NgramFrequencyScorer(freq=ENGLISH_DIGRAMS)
    # Get every Caesar shift of the ciphertext
    shifts = [CaesarCipher(n).decrypt(text) for n in range(26)]

    # Score each shift according to English character frequency.
    # Get tuples that pair the score with the text.
    scored_shifts = [(scorer.score(shift), shift) for shift in shifts]

    # Sort by score, descending order
    scored_shifts.sort(reverse=True)

    output["decrypted"] = scored_shifts[0]

    return output