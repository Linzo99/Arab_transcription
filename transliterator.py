import alphabet
from mapping import _mapping
from ArabText import ArabicText


def normalize(text):
    # some text may have shadda coming after a vowel whic in this case
    # will fail the script, so were swapping
    text = list(text)
    for i, c in enumerate(text):
        if c == alphabet.SHADDA and (text[i-1] in alphabet.VOWELS):
            text[i], text[i-1] = text[i-1], text[i]
    return text


class ArabTransliterator:

    def __init__(self):
        self.table = _mapping

    def get(self, key):
        return self.table.get(key, '')

    def translate(self, text):
        out = [] 
        text = normalize(text)
        arabic_text = iter(ArabicText(text))

        for caracter in arabic_text:

            # handle hamza
            if caracter in alphabet.HAMZAS:
                if caracter.is_mid():
                    out.append(u"'")
                continue

            # handle lam
            elif caracter == alphabet.LAM:
                sun = caracter.is_sun()
                # handle alif lam
                if (p := caracter.prev()) == alphabet.ALIF:
                    sep = '-' if p.is_word_start() else ''
                    out.append("" if sun else "l"+sep)

                # handle alif with hamzat wasl
                elif (p := caracter.prev()) == alphabet.ALIF_WITH_HAMZAT_WASL:
                    out[-1] = u"a" if p.is_start() else "l-"

                else:
                    out.append("" if sun else "l")

                if sun:
                    sep = '-' if caracter.prev().is_word_start() else ''
                    out.append(sep.join([self.get(sun)]*2))
                    next(arabic_text)
                    next(arabic_text)

                continue

            # handle alif
            elif caracter == alphabet.ALIF:
                if caracter.prev() == alphabet.FATHA:
                    out[-1] = u"ā"
                continue

            # handle alif with hamzat wasl
            elif caracter == alphabet.ALIF_WITH_HAMZAT_WASL:
                out.append(u"i")
                continue

            # handle alif maksura
            elif caracter == alphabet.ALIF_MAKSURA:
                if caracter.prev() == alphabet.FATHA:
                    out[-1] = u"\u00E1"
                continue

            # handle alif with maddah above
            elif caracter == alphabet.ALIF_WITH_MADDA_ABOVE:
                out.append(u'ā' if caracter.is_start() else u'’ā')
                continue

            # kasra + ya
            elif caracter.is_kasra_followed_by_ya():
                if caracter.next(2) not in alphabet.VOWELS:
                    out.append(u'ī')
                    next(arabic_text)
                else:
                    out.append(u'i')
                continue

            # damma + waw
            elif caracter.is_damma_followed_by_waw():
                if caracter.next(2) not in alphabet.VOWELS:
                    out += u'ū'
                    next(arabic_text)
                else:
                    out.append(u'u')
                continue

            # handle SHADDA
            elif caracter == alphabet.SHADDA:
                vow = caracter.prev(2)
                # if preceded by YA
                if caracter.prev() == alphabet.YA:
                    if vow == alphabet.KASRA and caracter.is_mid():
                        out.append(u"y")

                    elif vow == alphabet.FATHA:
                        out.append(u"y")

                # if preceded by WAW
                elif caracter.prev() == alphabet.WAW:
                    if vow == alphabet.DAMMA:
                        out.append(u"w")

                    elif vow == alphabet.FATHA:
                        out.append(u"w")

                elif caracter.prev().is_mid():
                    if len(out) > 2 and (not out[-2] == "l-"):
                        out.append(self.get(str(caracter.prev())))

            # handle the rest
            else:
                out.append(self.get(str(caracter)))
                if caracter.next() in (alphabet.SUKUN, alphabet.SMALL_HIGH_ROUNDED_ZERO):
                    if caracter.prev() == alphabet.ALIF and caracter.prev().is_word_start():
                        out[-1] = self.get(str(caracter))+'-'

        return "".join(out)


if __name__ == "__main__":
    from pathlib import Path
    import argparse

    translator = ArabTransliterator()

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="The arab file you want the transcription")
    parser.add_argument("-t", "--text", help="The arab text you want the transcription")
    args = parser.parse_args()

    if args.file:
        file = Path(args.file)
        lines = file.read_bytes().decode("utf-8").split("\n")
        print(*map(translator.translate, lines), sep="\n")

    elif args.text:
        print(translator.translate(args.text))
