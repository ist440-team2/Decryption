test_cases = [
    {
        "name"          : "english_simple",
        "ocr_bucket"    : "ist440grp2ocr",
        "ocr_key"       : "jen_zodiacTest1.txt",
        "language"      : "en",
        "encrypted"     : "Nokb Onsdyb, Drsc sc dro Jynskm czokusxq. Sx kxcgob dy iyeb kcusxq pyb wybo nodksvc klyed dro qyyn dswoc S rkfo rkn sx Fkvvoty, S crkvv lo fobi rkzzi dy cezzvi ofox wybo wkdobskv. Li dro gki, kbo dro zyvsmo rkfosxq k qyyn dswo gsdr dro myno? Sp xyd, dovv drow dy mroob ez; grox droi ny mbkmu sd droi gsvv rkfo wo.",
        "decrypted"     : "DEAR EDITOR, THIS IS THE ZODIAC SPEAKING. IN ANSWER TO YOUR ASKING FOR MORE DETAILS ABOUT THE GOOD TIMES I HAVE HAD IN VALLEJO, I SHALL BE VERY HAPPY TO SUPPLY EVEN MORE MATERIAL. BY THE WAY, ARE THE POLICE HAVEING A GOOD TIME WITH THE CODE? IF NOT, TELL THEM TO CHEER UP; WHEN THEY DO CRACK IT THEY WILL HAVE ME."
    },
    {
        "name"          : "english_garbage_word",
        "ocr_bucket"    : "ist440grp2ocr",
        "ocr_key"       : "jen_english_with_garbage.txt",
        "language"      : "en",
        "encrypted"     : "aopz pz alea aoha jvuahpuz h nhyihnl zhsrkqmszrhkqm dvyk.",
        "decrypted"     : "THIS IS TEXT THAT CONTAINS A GARBAGE SALKDJFLSKADJF WORD."
    },
    {
        "name"          : "spanish",
        "ocr_bucket"    : "ist440grp2ocr",
        "ocr_key"       : "jen_spanish",
        "language"      : "es",
        "encrypted"     : "Qr vrb dvhvlqr",
        "decrypted"     : "NO SOY ASESINO"
    },
{
        "name"          : "french",
        "ocr_bucket"    : "ist440grp2ocr",
        "ocr_key"       : "jen_french",
        "language"      : "fr",
        "encrypted"     : '''Krnw vxrwb sjuxdg mn unda bdaerean
Zdn mn yjacjpna unda lnaldnru,
Wxdb jdaxwb un bdkurvn xapdnru
Mn unb enwpna xd mn unb bdrean''',
        "decrypted"     : '''BIEN MOINS JALOUX DE LEUR SURVIVRE
QUE DE PARTAGER LEUR CERCUEIL,
NOUS AURONS LE SUBLIME ORGUEIL
DE LES VENGER OU DE LES SUIVRE'''
    }
]