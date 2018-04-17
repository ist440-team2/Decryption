#!/usr/bin/env python

import boto3
from etao440 import CaesarCipher, NgramFrequencyScorer
from etao440.freq import ENGLISH_DIGRAMS, ENGLISH_FREQ
from Frequency import lang_di, lang_freq


def lambda_handler(event, context):
    """
    Invoked by Lambda

    :param event: contains the S3 bucket and key for the OCR file to be decrypted
    :param context: metadata associated with this Lambda/Step Function execution
    :return: a dictionary passed back to Lambda containing the input data, decrypted text, and confidence
    """

    method = "Caesar"
    output_bucket = "ist440grp2-decrypted"
    output_key_pattern = "%s_%s_%s"

    try:
        input_bucket = event["bucket"]
        input_key = event["key"]
    except KeyError:
        print("Bucket and key are required")
        exit(1)

    try:
        language = event["sourceLanguage"]
    except KeyError:
        print("Source language missing, assuming English")
        language = "en"

    output_key = output_key_pattern % (input_key, method, language)

    text = get_text(input_bucket, input_key)

    scorer = NgramFrequencyScorer(freq=lang_di(language))
    # Get every Caesar shift of the ciphertext
    shifts = [CaesarCipher(n).decrypt(text) for n in range(len(lang_freq(language)))]

    # Score each shift according to English character frequency.
    # Get tuples that pair the score with the text.
    scored_shifts = [(scorer.score(shift), shift) for shift in shifts]

    # Sort by score, descending order
    scored_shifts.sort(reverse=True)

    save_text(output_bucket, output_key, scored_shifts[0][1])
    print(scored_shifts[0][1])

    output = {
        "method": method,
        "confidence": scored_shifts[0][0],
        "decryptedBucket": output_bucket,
        "decryptedKey": output_key,
        "sourceLanguage": "en"
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
