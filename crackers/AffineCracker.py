import string
from math import gcd

from ciphers.AffineCipher import AffineCipher
from crackers.BruteCracker import BruteCracker


class AffineCracker(BruteCracker):
    def __init__(self, alphabet=string.ascii_uppercase):
        super().__init__(AffineCipher, alphabet)

    def generate_keys(self):
        for a in range(len(self.alphabet)):
            if gcd(a, len(self.alphabet)) > 1:
                continue
            for b in range(len(self.alphabet)):
                yield a, b


if __name__ == '__main__':
    print(AffineCracker().crack("wellhellotheremyfriend!".upper()))
    print(AffineCracker().crack(AffineCipher((11, 8)).encrypt("hopefullythisworks".upper())))
