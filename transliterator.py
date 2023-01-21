import alphabet
from mapping import _mapping
from ArabText import ArabicText

class ArabTransliterator:

    def __init__(self):
        self.table = _mapping

    def get(self, key):
        return self.table.get(key, '')

    def translate(self, text):

        out = [] 
        arabic_text = iter(ArabicText(text))
        #  for c in arabic_text: print(c, end="")

        for caracter in arabic_text:

            # handle hamza
            if caracter in (alphabet.HAMZA, alphabet.ALIF_WITH_HAMZA_ABOVE, alphabet.ALIF_WITH_HAMZA_BELOW):
                if caracter.is_mid():
                    out.append(u"'")
                else:
                    continue

            # handle alif
            elif caracter == alphabet.ALIF:
                # handle alif lam
                if caracter.next() == alphabet.LAM:
                    # handle long alif
                    if caracter.prev() == alphabet.FATHA: 
                        out[-1] = u"ā"
                    else:
                        if caracter.is_start():
                            out.append("a")
                        if c:=caracter.is_followed_by_sun():
                            out.append('-'.join([self.get(c)]*2))
                            next(arabic_text)
                            next(arabic_text)
                        else:
                            out.append(u'l-')
                        next(arabic_text)
                # followed by sukun
                elif caracter.next() in (alphabet.SUKUN, alphabet.SMALL_HIGH_ROUNDED_ZERO):
                    next(arabic_text)
                    continue
                # preceeded by fathatan
                elif caracter.prev() in alphabet.TANWIN:
                    continue
                # preceeded by fatha
                elif caracter.prev() == alphabet.FATHA:
                    out[-1] = u"ā"
                    continue

            # handle alif with hamzat wasl
            elif caracter == alphabet.ALIF_WITH_HAMZAT_WASL:
                if caracter.next() == alphabet.LAM:
                    if caracter.is_start(): 
                        out.append(u"a")
                    else:
                        out.append("l-")
                        next(arabic_text)
                else:
                    out.append(u"i")

            # kasra + ya
            elif caracter.is_kasra_followed_by_ya():
                out.append(u'ī')
                next(arabic_text)
                continue

            # damma + wa
            elif caracter.is_damma_followed_by_waw():
                if caracter.next(2) in alphabet.VOWELS:
                    out.append(u"uw")
                else:
                    out += u'ū'
                    if caracter.next(2) == alphabet.SHADDA:
                        out.append(u'w')
                next(arabic_text)
                continue

            # handle alif with maddah above
            elif caracter == alphabet.ALIF_WITH_MADDA_ABOVE:
                if caracter.is_start():
                    out.append(u'ā')
                elif caracter.is_mid():
                    out += u'’ā'

            # handle TA_MARBUTA
            elif caracter == alphabet.TA_MARBUTA:
                # space + laam + 'alif
                if caracter.succeeded(3) == u" "+alphabet.LAM+alphabet.ALIF:
                    out.append(u"t")
                # fatha/damma/kasra + space + laam + 'alif
                elif caracter.next() in alphabet.VOWELS and caracter.next().succeeded(3) == u" "+alphabet.LAM+alphabet.ALIF:
                    out.append(u"t")
                # Fathatayn, Dammatayn, kasratayn
                elif caracter.next() in alphabet.TANWIN:
                    out.append(u"t")
                else:
                    out.append(u"h")

            # handle ALIF_MAKSURA
            elif caracter == alphabet.ALIF_MAKSURA:
                # preceeded by Fatha
                if caracter.prev() == alphabet.FATHA:
                    out[-1] = u"\u00E1"

            # handle SHADDA
            elif caracter == alphabet.SHADDA:
                if caracter.prev() == alphabet.ALIF_MAKSURA:
                    if (p:=caracter.prev(2)) == alphabet.KASRA:
                        if p.is_mid():
                            out.append(u"y")
                        elif p.is_end():
                            out[-1] = u"ī"
                    elif caracter.prev().is_mid():
                        out.append(self.get(str(caracter.prev())))
                elif caracter.prev().is_mid():
                    out.append(self.get(str(caracter.prev())))

            # handle the rest
            else:
                out.append(self.get(str(caracter)))

        return "".join(out)


if __name__ == "__main__":
    import sys
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
        print(*map(translator().translate, lines), sep="\n")

    elif args.text:
        print(translator.translate(args.text))
