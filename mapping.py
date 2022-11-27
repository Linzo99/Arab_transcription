import alphabet

_mapping = {
    alphabet.HAMZA: u'\'',
    alphabet.ALIF: u'',
    alphabet.ALIF_WITH_MADDA_ABOVE: chr(0x0100),
    alphabet.ALIF_WITH_HAMZA_ABOVE: u'\'',
    alphabet.WAW_WITH_HAMZA_ABOVE: u'\'',
    alphabet.ALIF_WITH_HAMZA_BELOW: u'\'',
    alphabet.YA_WITH_HAMZA_ABOVE: u'\'',  # Ya with Hamza ABOVE
    # NOTE: Alif doesn't seem to have transcription in ALA-LC, so I am using the
    # same one for Alif with Madda.
    alphabet.BA: u'b',  # Ba
    alphabet.TA_MARBUTA: chr(0x1e97),
    alphabet.TA: u't',
    alphabet.THA: u'th',
    alphabet.JEEM: u'j',
    alphabet.HHA: chr(0x1e25),
    alphabet.KHA: u'kh',
    alphabet.DAL: u'd',
    alphabet.THAL: u'dh',
    alphabet.RA: u'r',
    alphabet.ZAY: u'z',
    alphabet.SEEN: u's',
    alphabet.SHEEN: u'sh',
    alphabet.SAD: chr(0x1e63),
    alphabet.DAD: chr(0x1e0d),
    alphabet.TAH: chr(0x1e6d),
    alphabet.ZAH: chr(0x1e93),
    alphabet.AIN: chr(0x02bf),
    alphabet.GHAIN: u'gh',
    # Removing Tatweel in the transcription
    alphabet.TATWEEL: u'',
    alphabet.FA: u'f',
    alphabet.QAF: u'q',
    alphabet.KAF: u'k',
    alphabet.LAM: u'l',
    alphabet.MEEM: u'm',
    alphabet.NOON: u'n',
    alphabet.HA: u'h',
    alphabet.WAW: u'w',
    alphabet.ALIF_MAKSURA: u'',
    alphabet.YA: u'y',
    alphabet.FATHATAN: u'an',   # Rafid
    alphabet.DAMMATAN: u'un',   # Rafid
    alphabet.KASRATAN: u'in',   # Rafid
    alphabet.FATHA: u'a',
    alphabet.DAMMA: u'u',
    alphabet.KASRA: u'i',
    # Shadda in ALA-LC is represented by doubling the letter.
    #alphabet.SHADDA: chr(),  # Shadda
    # Sukon in ALA-LC doesn't have a representation in ALA-LC.
    alphabet.SUKUN: u'',  # Sukun
    # Alif Khanjariya
    alphabet.ALIF_KHANJAREEYA: chr(0x0101),  # Alif Khanjariya
    # TODO: Implement the transcription of Hamzat Al-Wasl
    alphabet.ALIF_WITH_HAMZAT_WASL: u'i',
    # The following letters don't have a representation in ALA-LC.
    alphabet.HAMZAABOVE: u'',
    alphabet.SMALL_HIGH_SEEN: u'',
    alphabet.SMALL_HIGH_ROUNDED_ZERO: u'',
    alphabet.SMALL_HIGH_UPRIGHT_RECTANGULAR_ZERO_: u'',
    alphabet.SMALL_HIGH_MEEM_ISOLATED_FORM: u'',
    alphabet.SMALL_LOW_SEEN: u'',
    alphabet.SMALL_WAW: u'',
    alphabet.SMALL_YA: u'',
    alphabet.SMALL_HIGH_NOON: u'',
    alphabet.EMPTY_CENTRE_LOW_STOP: u'',
    alphabet.EMPTY_CENTRE_HIGH_STOP: u'',
    alphabet.ROUNDED_HIGH_STOP_WITH_FILLED_CENTRE: u'',
    alphabet.SMALL_LOW_MEEM: u''
}

def get_char(key):
    return _mapping.get(key, '')
