from unittest import TestCase
import DecryptCaesar
import boto3

test_cases = [
    ("english_simple",
     "ist440grp2ocr",
     "jen_zodiacTest1.txt",
     "Nokb Onsdyb, Drsc sc dro Jynskm czokusxq. Sx kxcgob dy iyeb kcusxq pyb wybo nodksvc klyed dro qyyn dswoc S rkfo rkn sx Fkvvoty, S crkvv lo fobi rkzzi dy cezzvi ofox wybo wkdobskv. Li dro gki, kbo dro zyvsmo rkfosxq k qyyn dswo gsdr dro myno? Sp xyd, dovv drow dy mroob ez; grox droi ny mbkmu sd droi gsvv rkfo wo.",
     "DEAR EDITOR, THIS IS THE ZODIAC SPEAKING. IN ANSWER TO YOUR ASKING FOR MORE DETAILS ABOUT THE GOOD TIMES I HAVE HAD IN VALLEJO, I SHALL BE VERY HAPPY TO SUPPLY EVEN MORE MATERIAL. BY THE WAY, ARE THE POLICE HAVEING A GOOD TIME WITH THE CODE? IF NOT, TELL THEM TO CHEER UP; WHEN THEY DO CRACK IT THEY WILL HAVE ME."),
    ("english_garbage_word",
     "ist440grp2ocr",
     "jen_english_with_garbage.txt",
     "aopz pz alea aoha jvuahpuz h nhyihnl zhsrkqmszrhkqm dvyk.",
     "THIS IS TEXT THAT CONTAINS A GARBAGE SALKDJFLSKADJF WORD.")
]
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