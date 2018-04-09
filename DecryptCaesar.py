#!/usr/bin/env python

import boto3
from etao import CaesarCipher, NgramFrequencyScorer
from etao.freq import ENGLISH_DIGRAMS

method = "etao-decryptCaesar"

def lambda_handler(event, context):
    """
    Invoked by Lambda

    :param event: contains the S3 bucket and key for the OCR file to be decrypted
    :param context: metadata associated with this Lambda/Step Function execution
    :return: a dictionary passed back to Lambda containing the input data, decrypted text, and confidence
    """

    output_key = event["key"] + "_" + method

    text = get_text(event["bucket"], event["key"])

    scorer = NgramFrequencyScorer(freq=ENGLISH_DIGRAMS)
    # Get every Caesar shift of the ciphertext
    shifts = [CaesarCipher(n).decrypt(text) for n in range(26)]

    # Score each shift according to English character frequency.
    # Get tuples that pair the score with the text.
    scored_shifts = [(scorer.score(shift), shift) for shift in shifts]

    # Sort by score, descending order
    scored_shifts.sort(reverse=True)

    save_text("ist440grp2-decrypted", event["key"], scored_shifts[0][1])

    output = {
        "method": method,
        "confidence": scored_shifts[0][0],
        "decrypted_bucket": "ist440grp2-decrypted",
        "decrypted_key": event["key"]
    }

    return output


def get_text(bucket, key):
    """
    Retrieves the specified file in S3 containing the text output by the OCR module

    :param bucket: the S3 bucket
    :param key: the S3 key (file name)
    :return: a string containing the text
    """
    s3 = boto3.resource("s3")

    ocr_obj = s3.Object(bucket,key)
    response = ocr_obj.get()
    data = response["Body"].read()

    return data


def save_text(bucket, key, data):
    """
    Saves data to S3
    :param bucket: the S3 bucket
    :param key: the S3 key (file name)
    :param data: the data to save
    :return:
    """

    s3 = boto3.resource("s3")
    s3.Bucket(bucket).put_object(Key=key, Body=data)
