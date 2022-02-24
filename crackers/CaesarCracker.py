import string

from ciphers.CaesarCipher import CaesarCipher
from crackers.BruteCracker import BruteCracker


class CaesarCracker(BruteCracker):
    def __init__(self, alphabet=string.ascii_uppercase):
        super().__init__(CaesarCipher, alphabet)

    def generate_keys(self):
        for i in range(len(self.alphabet)):
            yield i


if __name__ == '__main__':
    print(CaesarCracker().crack("wellhellotheremyfriend!".upper()))
    print(CaesarCracker().crack(CaesarCipher(11).encrypt("hopefullythisworks".upper())))
