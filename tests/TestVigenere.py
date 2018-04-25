from unittest import TestCase
from CasesVigenere import test_cases
from decryption.DecryptVigenere import DecryptVigenere


class TestVigenere(TestCase):

   def test_lambda_handler(self):

        for test_case in test_cases:
            print("test case: " + test_case["name"])

            d = DecryptVigenere()
            result = d.decrypt(test_case["encrypted"], test_case["language"])
            self.assertEqual(test_case["decrypted"], result["text"])
            self.assertTrue(result["confidence"] >= 0)
            self.assertTrue(result["confidence"] <= 1)
