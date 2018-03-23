from unittest import TestCase
from decrypt import DecryptCaesar


class TestCaesar(TestCase):
    """
    Test cases for DecryptCaesar
    """

    def test_lambda_handler(self):

        inputEvent = {
            "userId": "testuser",
            "inputText": "Nokb Onsdyb, Drsc sc dro Jynskm czokusxq. Sx kxcgob dy iyeb kcusxq pyb wybo nodksvc klyed dro qyyn dswoc S rkfo rkn sx Fkvvoty, S crkvv lo fobi rkzzi dy cezzvi ofox wybo wkdobskv. Li dro gki, kbo dro zyvsmo rkfosxq k qyyn dswo gsdr dro myno? Sp xyd, dovv drow dy mroob ez; grox droi ny mbkmu sd droi gsvv rkfo wo."
        }

        inputContext = {"test": "test"}
        expectedResult = "DEAR EDITOR, THIS IS THE ZODIAC SPEAKING. IN ANSWER TO YOUR ASKING FOR MORE DETAILS ABOUT THE GOOD TIMES I HAVE HAD IN VALLEJO, I SHALL BE VERY HAPPY TO SUPPLY EVEN MORE MATERIAL. BY THE WAY, ARE THE POLICE HAVEING A GOOD TIME WITH THE CODE? IF NOT, TELL THEM TO CHEER UP; WHEN THEY DO CRACK IT THEY WILL HAVE ME."

        result = DecryptCaesar.lambda_handler(inputEvent, inputContext)
        self.assertEqual(expectedResult, result['decrypted'][1])
