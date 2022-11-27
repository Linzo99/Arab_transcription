from io import StringIO

import alphabet
from mapping import _mapping, get_char

from arabic_text import ArabicText


def to_phonetic(string):
    """
     Return the transliteration of given arab text.
    :param string: The string to be converted.
    :return The phonetic representation of the string.
    """
    string_buffer = StringIO()
    arabic_text = iter(ArabicText(string))

    for caracter in arabic_text:
        # Whitespace
        if caracter.is_blank():
            string_buffer.write(u' ')
            continue

        # Handle Ta Marbuta
        if caracter == alphabet.TA_MARBUTA:
            # Ta Marbuta is transcribed as either 't' or 'h' depending on the context.
            string_buffer.write(u't')
            continue

        # Handle Alif
        if caracter.is_alif():
            # verify it its ALIF LAM
            if caracter.is_al():
                if caracter.is_word_start():
                    string_buffer.write(u'a')
                if c:=caracter.is_followed_by_sun():
                    string_buffer.write(u''+'-'.join([get_char(c)]*2))
                    next(arabic_text)
                else:
                    string_buffer.write(u'l-')

                # Skip the next letter (Lam) because we already processed it.
                next(arabic_text)
                continue

            elif caracter.next() == alphabet.SUKUN or caracter.next() == alphabet.SMALL_HIGH_ROUNDED_ZERO:
                next(arabic_text)
                continue
            
            elif caracter.is_word_start():
                string_buffer.write(u'i')
                continue

            # Handle Alif with Madda
            elif caracter == alphabet.ALIF_WITH_MADDA_ABOVE:
                # Alif with Madda at the beginning of a word is replaced with ā
                if caracter.is_word_start():
                    string_buffer.write(u'ā')
                else:
                    string_buffer.write(u'a')
                continue

        if caracter.is_fatha_followed_by_alif():
            # Treat like an Alif.
            string_buffer.write(u'ā')
            next(arabic_text)
            continue

        if caracter.is_kasra_followed_by_ya():
            # Treat like a Ya
            string_buffer.write(u'ī')
            next(arabic_text)
            continue

        if caracter.is_damma_followed_by_waw():
            # Treat like a Waw
            string_buffer.write(u'ū')
            next(arabic_text)
            continue

        if caracter == alphabet.FATHATAN or caracter == alphabet.DAMMATAN or \
                caracter == alphabet.KASRATAN:
            string_buffer.write(get_char(caracter.char()))
            if caracter.next().is_alif():
                next(arabic_text)
            continue

        # Handle the rest
        if caracter.char() in _mapping:
            count = 1
            if caracter.is_followed_by_shadda() and not caracter.prev().is_blank():
                count = 2
            string_buffer.write(get_char(caracter.char())*count)

    phonetic = string_buffer.getvalue()
    # TODO: Need to ensure we close the string buffer if an exception happens
    # before we reach this statement.
    string_buffer.close()
    return phonetic


if __name__ == "__main__":
    import sys
    from pathlib import Path
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="The arab file you want the transcription")
    parser.add_argument("-t", "--text", help="The arab text you want the transcription")
    args = parser.parse_args()

    if args.file:
        file = Path(args.file)
        lines = file.read_bytes().decode("utf-8").split("\n")
        print(*map(to_phonetic, lines), sep="\n")

    elif args.text:
        print(to_phonetic(args.text))
