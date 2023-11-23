from . import alphabet

_mapping = {
    #  alphabet.HAMZA: u'\'',
    #  alphabet.ALIF: u'',
    #  alphabet.ALIF_WITH_MADDA_ABOVE: chr(0x0100),
    #  alphabet.ALIF_WITH_HAMZA_ABOVE: u'\'',
    alphabet.WAW_WITH_HAMZA_ABOVE: "'",
    #  alphabet.ALIF_WITH_HAMZA_BELOW: u'\'',
    alphabet.YA_WITH_HAMZA_ABOVE: "'",  # Ya with Hamza ABOVE
    alphabet.BA: "b",  # Ba
    alphabet.TA_MARBUTA: "t",
    alphabet.TA: "t",
    alphabet.THA: "th",
    alphabet.JEEM: "j",
    alphabet.HHA: chr(0x1E25),
    alphabet.KHA: "kh",
    alphabet.DAL: "d",
    alphabet.THAL: "dh",
    alphabet.RA: "r",
    alphabet.ZAY: "z",
    alphabet.SEEN: "s",
    alphabet.SHEEN: "sh",
    alphabet.SAD: chr(0x1E63),
    alphabet.DAD: chr(0x1E0D),
    alphabet.TAH: chr(0x1E6D),
    alphabet.ZAH: chr(0x1E93),
    alphabet.AIN: chr(0x02BF),
    alphabet.GHAIN: "gh",
    #  alphabet.TATWEEL: u'',
    alphabet.FA: "f",
    alphabet.QAF: "q",
    alphabet.KAF: "k",
    alphabet.LAM: "l",
    alphabet.MEEM: "m",
    alphabet.NOON: "n",
    alphabet.HA: "h",
    alphabet.WAW: "w",
    #  alphabet.ALIF_MAKSURA: u'',
    alphabet.YA: "y",
    alphabet.FATHATAN: "an",  # Rafid
    alphabet.DAMMATAN: "un",  # Rafid
    alphabet.KASRATAN: "in",  # Rafid
    alphabet.FATHA: "a",
    alphabet.DAMMA: "u",
    alphabet.KASRA: "i",
    #  Shadda in ALA-LC is represented by doubling the letter.
    #  alphabet.SHADDA: chr(),  # Shadda
    alphabet.SUKUN: "",  # Sukun
    #  Alif Khanjariya
    #  alphabet.ALIF_KHANJAREEYA: chr(0x0101),  # Alif Khanjariya
    #  alphabet.ALIF_WITH_HAMZAT_WASL: u'',
    # The following letters don't have a representation in ALA-LC.
    #  alphabet.HAMZAABOVE: u'',
    #  alphabet.SMALL_HIGH_SEEN: u'',
    #  alphabet.SMALL_HIGH_ROUNDED_ZERO: u'',
    #  alphabet.SMALL_HIGH_UPRIGHT_RECTANGULAR_ZERO_: u'',
    #  alphabet.SMALL_HIGH_MEEM_ISOLATED_FORM: u'',
    #  alphabet.SMALL_LOW_SEEN: u'',
    #  alphabet.SMALL_WAW: u'',
    #  alphabet.SMALL_YA: u'',
    #  alphabet.SMALL_HIGH_NOON: u'',
    #  alphabet.EMPTY_CENTRE_LOW_STOP: u'',
    #  alphabet.EMPTY_CENTRE_HIGH_STOP: u'',
    #  alphabet.ROUNDED_HIGH_STOP_WITH_FILLED_CENTRE: u'',
    #  alphabet.SMALL_LOW_MEEM: u''
    " ": " ",
    # WOLOFAL CARACTERS
    alphabet.PEH: "p",
    alphabet.CEH: "c",
    alphabet.GNEH: "ñ",
    alphabet.GAF: "g",
    alphabet.EH: "é",
    alphabet.OH: "o",
}
