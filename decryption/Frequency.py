# -*- coding: utf-8 -*-

from etao440.freq import ENGLISH_FREQ, ENGLISH_DIGRAMS

""" From http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages """

SPANISH_FREQ = {
    u'a': 11.72,
    u'b': 1.49,
    u'c': 3.87,
    u'd': 4.67,
    u'e': 13.72,
    u'f': 0.69,
    u'g': 1.00,
    u'h': 1.18,
    u'i': 5.28,
    u'j': 0.52,
    u'k': 0.11,
    u'l': 5.24,
    u'm': 3.08,
    u'n': 6.83,
    u'o': 8.44,
    u'p': 2.89,
    u'q': 1.11,
    u'r': 6.41,
    u's': 7.20,
    u't': 4.60,
    u'u': 4.55,
    u'v': 1.05,
    u'w': 0.04,
    u'x': 0.14,
    u'y': 1.09,
    u'z': 0.47,
    u'á': 0.44,
    u'é': 0.36,
    u'í': 0.70,
    u'ñ': 0.17,
    u'ó': 0.76,
    u'ú': 0.12,
    u'ü': 0.02
}

SPANISH_DIGRAMS = {
    'de' :  2.57,
    'es' :  2.31,
    'en' :  2.27,
    'el' :  2.01,
    'la' :  1.80,
    'os' :  1.79,
    'on' :  1.61,
    'as' :  1.56,
    'er' :  1.52,
    'ra' :  1.47,
    'ad' :  1.43,
    'ar' :  1.43,
    're' :  1.42,
    'al' :  1.33,
    'an' :  1.24,
    'nt' :  1.22,
    'ue' :  1.21,
    'ci' :  1.15,
    'co' :  1.13,
    'se' :  1.11,
    'ta' :  1.09,
    'te' :  1.00,
    'or' :  0.98,
    'do' :  0.98,
    'io' :  0.98,
    'ac' :  0.96,
    'st' :  0.95,
    'na' :  0.92,
    'ro' :  0.85,
    'un' :  0.84
}

FRENCH_FREQ = {
    "a" :  7.60,
    "à" :  0.43,
    "â" :  0.05,
    "æ" :  0.00,
    "b" :  0.96,
    "c" :  3.39,
    "ç" :  0.05,
    "d" :  4.08,
    "e" : 14.47,
    "é" :  2.43,
    "è" :  0.42,
    "ê" :  0.13,
    "ë" :  0.00,
    "f" :  1.12,
    "g" :  1.18,
    "h" :  0.93,
    "i" :  7.21,
    "î" :  0.04,
    "ï" :  0.01,
    "j" :  0.30,
    "k" :  0.16,
    "l" :  5.86,
    "m" :  2.78,
    "n" :  7.32,
    "o" :  5.39,
    "ô" :  0.05,
    "œ" :  0.02,
    "p" :  2.98,
    "q" :  0.85,
    "r" :  6.86,
    "s" :  7.98,
    "t" :  7.11,
    "u" :  5.55,
    "ù" :  0.02,
    "û" :  0.02,
    "ü" :  0.00,
    "v" :  1.29,
    "w" :  0.08,
    "x" :  0.43,
    "y" :  0.34,
    "ÿ" :  0.00,
    "z" :  0.10
}

FRENCH_DIGRAMS = {
    "es" :  2.91,
    "le" :  2.08,
    "de" :  2.02,
    "en" :  1.97,
    "on" :  1.70,
    "nt" :  1.69,
    "re" :  1.62,
    "an" :  1.28,
    "la" :  1.25,
    "er" :  1.21,
    "te" :  1.19,
    "el" :  1.15,
    "se" :  1.09,
    "ti" :  1.04,
    "ur" :  1.01,
    "et" :  0.96,
    "ne" :  0.96,
    "is" :  0.94,
    "ed" :  0.93,
    "ou" :  0.93,
    "ar" :  0.88,
    "in" :  0.87,
    "it" :  0.86,
    "st" :  0.86,
    "qu" :  0.84,
    "ns" :  0.82,
    "ai" :  0.81,
    "me" :  0.79,
    "ra" :  0.79,
    "ie" :  0.76
}


def lang_freq(x):
    return {
        'en': ENGLISH_FREQ,
        'es': SPANISH_FREQ,
        'fr': FRENCH_FREQ
    }.get(x, ENGLISH_FREQ)


def lang_di(x):
    return {
        'en': ENGLISH_DIGRAMS,
        'es': SPANISH_DIGRAMS,
        'fr': FRENCH_DIGRAMS
    }.get(x, ENGLISH_DIGRAMS)
