import string
from math import gcd

from ciphers.AffineCipher import AffineCipher
from crackers.Cracker import Cracker
from text_fitness.quadgram_score import quadgram_score


class AffineCracker(Cracker):
    def __init__(self, alphabet=string.ascii_uppercase):
        super(AffineCracker, self).__init__(alphabet)

    def crack(self, ciphertext: str) -> tuple:
        solutions = []
        for a in range(len(self.alphabet)):
            if gcd(a, len(self.alphabet)) > 1:
                continue
            for b in range(len(self.alphabet)):
                plaintext = AffineCipher((a, b), self.alphabet).decrypt(ciphertext)
                solutions.append((quadgram_score(plaintext), (a, b), plaintext))
        solutions.sort(reverse=True)
        return solutions[0]


if __name__ == '__main__':
    print(AffineCracker().crack("wellhellotheremyfriend!".upper()))
    print(AffineCracker().crack(AffineCipher((11, 8)).encrypt("hopefullythisworks".upper())))
