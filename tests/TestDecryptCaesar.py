from unittest import TestCase
from decrypt import DecryptCaesar

test_cases = [
    ("english_simple",
     "Nokb Onsdyb, Drsc sc dro Jynskm czokusxq. Sx kxcgob dy iyeb kcusxq pyb wybo nodksvc klyed dro qyyn dswoc S rkfo rkn sx Fkvvoty, S crkvv lo fobi rkzzi dy cezzvi ofox wybo wkdobskv. Li dro gki, kbo dro zyvsmo rkfosxq k qyyn dswo gsdr dro myno? Sp xyd, dovv drow dy mroob ez; grox droi ny mbkmu sd droi gsvv rkfo wo.",
     "DEAR EDITOR, THIS IS THE ZODIAC SPEAKING. IN ANSWER TO YOUR ASKING FOR MORE DETAILS ABOUT THE GOOD TIMES I HAVE HAD IN VALLEJO, I SHALL BE VERY HAPPY TO SUPPLY EVEN MORE MATERIAL. BY THE WAY, ARE THE POLICE HAVEING A GOOD TIME WITH THE CODE? IF NOT, TELL THEM TO CHEER UP; WHEN THEY DO CRACK IT THEY WILL HAVE ME."),
    ("english_garbage_word",
    "aopz pz alea aoha jvuahpuz h nhyihnl zhsrkqmszrhkqm dvyk.",
     "THIS IS TEXT THAT CONTAINS A GARBAGE SALKDJFLSKADJF WORD.")
]

test_context = {"test": "test"}


class TestCaesar(TestCase):
    """
    Test cases for DecryptCaesar
    """

    def test_lambda_handler(self):
        for test_case in test_cases:
            result = DecryptCaesar.lambda_handler({"inputText": test_case[1]}, test_context)
        self.assertEqual(test_case[2], result['decrypted'][1])
