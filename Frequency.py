# -*- coding: utf-8 -*-

from etao440.freq import ENGLISH_FREQ, ENGLISH_DIGRAMS

"""From https://www.sttmedia.com/characterfrequency-spanish"""
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

""" From http://practicalcryptography.com/cryptanalysis/letter-frequencies-various-languages/spanish-letter-frequencies/ """
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


def lang_freq(x):
    return {
        'en': ENGLISH_FREQ,
        'ES': SPANISH_FREQ
    }.get(x, ENGLISH_FREQ)


def lang_di(x):
    return {
        'en': ENGLISH_DIGRAMS,
        'ES': SPANISH_DIGRAMS
    }.get(x, ENGLISH_DIGRAMS)
