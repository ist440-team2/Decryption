from unittest import TestCase
from cases import test_cases
from decryption import DecryptCaesar

test_context = {"test": "test"}
test_method = "Caesar"
output_bucket = "ist440grp2-decrypted"


class TestCaesar(TestCase):
    """
    Test cases for DecryptCaesar
    """

    def test_lambda_handler(self):

        for test_case in test_cases:
            print("test case: " + test_case["name"])
            result =  DecryptCaesar.lambda_handler(test_case["encrypted"], test_case["language"])
            self.assertEqual(test_case["decrypted"], result["text"])
            self.assertTrue(result["confidence"] >= 0)
            self.assertTrue(result["confidence"] <= 1)