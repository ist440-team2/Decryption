from unittest import TestCase
from CasesVigenere import test_cases
import DecryptCaesar
import boto3

test_context = {"test": "test"}
test_method = "Caesar"
output_bucket = "ist440grp2-decrypted"


class TestVigenere(TestCase):
    """
    Test cases for DecryptCaesar
    """

    def test_lambda_handler(self):


    def test_lambda_handler(self):

        for test_case in test_cases:
            print("test case: " + test_case["name"])
            event = {
                "bucket": test_case["ocr_bucket"],
                "key": test_case["ocr_key"],
                "sourceLanguage": test_case["language"]
            }

            # test the lambda function's output
            result = DecryptVigenere.lambda_handler(event, test_context)
            self.assertEqual(output_bucket, result["decryptedBucket"])
            self.assertEqual("%s_%s_%s" % (test_case["ocr_key"], "Caesar", test_case["language"]), result["decryptedKey"])
            self.assertEqual(test_method, result["method"])
            self.assertTrue(result["confidence"] >= 0)
            self.assertTrue(result["confidence"] <= 1)

            # test the output written to s3
            s3 = boto3.resource("s3")
            obj = s3.Object(result["decryptedBucket"], result["decryptedKey"])
            response = obj.get()
            data = response["Body"].read()
            self.assertEqual(test_case["decrypted"], data)

            # clean up
            s3.Object(result["decryptedBucket"], result["decryptedKey"]).delete()

    # def test_get_text(self):
    #     print("test_get_text")
    #     DecryptCaesar.get_text("ist440grp2ocr", "jen_zodiacTest1.txt")
    #
    # def test_missingBucket(self):
    #     print("test_missingBucket")
    #     input = {
    #         "key": "test"
    #     }
    #     result = DecryptCaesar.lambda_handler(input, test_context)
    #     self.assertEqual({'failed': 'true'}, result)
    #
    # def test_missing_file(self):
    #     print("test_missing_file")
    #     input = {
    #         "bucket": "ist440grp2ocr",
    #         "key": "nope",
    #         "sourceLanguage": "en"
    #     }
    #     result = DecryptCaesar.lambda_handler(input, test_context)
    #     self.assertEqual({'failed': 'true'}, result)