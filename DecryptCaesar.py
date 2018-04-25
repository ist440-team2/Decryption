#!/usr/bin/env python

import sys
import boto3
from botocore import exceptions
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

        try:
            language = event["sourceLanguage"]
        except KeyError:
            print("Source language missing, assuming English")
            language = "en"

        output_key = output_key_pattern % (input_key, method, language)
        text = get_text(input_bucket, input_key)

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

        save_text(output_bucket, output_key, highest["text"])

        output = {
            "method": method,
            "confidence": highest["confidence"],
            "decryptedBucket": output_bucket,
            "decryptedKey": output_key,
            "sourceLanguage": language
        }

        return output

    except exceptions.ClientError as err:
        print(err)
        output = {
            "failed": "true"
        }
        return output
    except:
        print("Unexpected error:", sys.exc_info()[0])
        output = {
            "failed": "true"
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

    ocr_obj = s3.Object(bucket, key)
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
    s3.Bucket(bucket).put_object(Key=key, Body=data, ACL='public-read', ContentType='text/plain')
