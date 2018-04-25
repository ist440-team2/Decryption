from unittest import TestCase
from decryption.Frequency import lang_di

class TestFrequency(TestCase):

    def test_lang_di(self):
        digrams = lang_di("en")
        self.assertEqual(1.52, digrams["th"])

        digrams = lang_di("fr")
        self.assertEqual(2.08, digrams["le"])

        digrams = lang_di("es")
        self.assertEqual(1.52, digrams["er"])