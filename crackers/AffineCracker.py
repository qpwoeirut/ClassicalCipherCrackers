import random
import string
from math import gcd

from ciphers.AffineCipher import AffineCipher
from crackers.BruteCracker import BruteCracker
from crackers.SubstitutionCracker import SubstitutionCracker


class AffineCracker(BruteCracker, SubstitutionCracker):
    def __init__(self, alphabet=string.ascii_uppercase):
        super().__init__(AffineCipher, alphabet)

    def decrypt(self, key, ciphertext: str) -> str:
        return AffineCipher(key).decrypt(ciphertext)

    def generate_random_key(self) -> tuple:
        a = random.randint(0, len(self.alphabet) - 1)
        while gcd(a, len(self.alphabet)) > 1:
            a = random.randint(0, len(self.alphabet) - 1)
        b = random.randint(0, len(self.alphabet) - 1)
        return a, b

    def generate_keys(self):
        for a in range(len(self.alphabet)):
            if gcd(a, len(self.alphabet)) > 1:
                continue
            for b in range(len(self.alphabet)):
                yield a, b


if __name__ == '__main__':
    print(AffineCracker().crack("wellhellotheremyfriend!".upper()))
    print(AffineCracker().crack(AffineCipher((11, 8)).encrypt("hopefullythisworks".upper())))
