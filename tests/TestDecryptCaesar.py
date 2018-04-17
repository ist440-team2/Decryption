from unittest import TestCase
from cases import test_cases
import DecryptCaesar
import boto3

test_context = {"test": "test"}
test_method = "Caesar"
output_bucket = "ist440grp2-decrypted"


class TestCaesar(TestCase):
    """
    Test cases for DecryptCaesar
    """

    def test_lambda_handler(self):

        for test_case in test_cases:
            event = {
                "bucket": test_case[1],
                "key": test_case[2]
            }

            # test the lambda function's output
            result = DecryptCaesar.lambda_handler(event, test_context)
            self.assertEqual(output_bucket, result["decryptedBucket"])
            self.assertEqual(test_case[2] + "_Caesar_en", result["decryptedKey"])
            self.assertEqual(test_method, result["method"])
            self.assertTrue(result["confidence"] >= 0)
            self.assertTrue(result["confidence"] <= 1)

            # test the output written to s3
            s3 = boto3.resource("s3")
            obj = s3.Object(result["decryptedBucket"], result["decryptedKey"])
            response = obj.get()
            data = response["Body"].read()
            self.assertEqual(test_case[4], data)

            # clean up
            s3.Object(result["decryptedBucket"], result["decryptedKey"]).delete()

    def test_get_text(self):
        DecryptCaesar.get_text("ist440grp2ocr", "jen_zodiacTest1.txt")

    def test_missingBucket(self):
        input = {
            "key": "test"
        }
        result = DecryptCaesar.lambda_handler(input, test_context)
        self.assertIsNotNone(result)