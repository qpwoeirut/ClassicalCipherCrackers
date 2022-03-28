import random
import time
from typing import Callable

from ciphers.AutokeyCipher import AutokeyCipher
from ciphers.Cipher import Cipher
from ciphers.ColumnarTranspositionCipher import ColumnarTranspositionCipher
from ciphers.MyszkowskiTranspositionCipher import MyszkowskiTranspositionCipher
from ciphers.PlayfairCipher import PlayfairCipher
from ciphers.VigenereCipher import VigenereCipher
from crackers.AutokeyCracker import AutokeyCracker
from crackers.ColumnarTranspositionCracker import ColumnarTranspositionCracker
from crackers.Cracker import Cracker
from crackers.MyszkowskiTranspositionCracker import MyszkowskiTranspositionCracker
from crackers.PlayfairCracker import PlayfairCracker
from crackers.VigenereCracker import VigenereCracker
from util import ALPHABET_IJ_MERGED

random.seed(0)  # seed to ensure easy reproducibility


class CrackerTester:
    def __init__(self, text: str, cipher_creator: Callable[[str], Cipher], cracker: Cracker):
        self.cipher_creator = cipher_creator
        self.cracker = cracker
        self.text = ''.join([x for x in cipher_creator("").filter_invalid(text)])

    def pick_random_excerpt(self):
        a = random.choice(range(len(self.text)))
        b = random.choice(range(len(self.text)))
        while a == b:
            b = random.choice(range(len(self.text)))

        return self.text[min(a, b):max(a, b)].strip().upper()

    def run_test(self, trials: int) -> float:
        plaintexts = [self.pick_random_excerpt() for _ in range(trials)]
        keys = [self.cracker.generate_random_key() for _ in range(trials)]
        ciphertexts = [self.cipher_creator(keys[i]).encrypt(plaintexts[i]) for i in range(trials)]

        start = time.time()
        decrypted = [self.cracker.crack(ciphertext) for ciphertext in ciphertexts]
        finish = time.time()

        for i in range(trials):
            assert decrypted[i][2] == plaintexts[i], f"\n{keys[i]}\n{decrypted[i][2]}\n{plaintexts[i]}"
            assert self.keys_match(decrypted[i][1], keys[i]), f"\n{keys[i]}\n{decrypted[i][2]}\n{plaintexts[i]}"

        return finish - start

    @staticmethod
    def keys_match(k1: str, k2: str) -> bool:
        if len(k1) >= len(k2):
            return k1 == k2 * (len(k1) // len(k2))
        else:
            return k2 == k1 * (len(k2) // len(k1))


def main():
    with open("rabbitsign_faq.txt") as f:
        text = f.read().strip()
    CrackerTester(text, AutokeyCipher, AutokeyCracker()).run_test(3)
    CrackerTester(text, VigenereCipher, VigenereCracker()).run_test(3)
    CrackerTester(text, ColumnarTranspositionCipher, ColumnarTranspositionCracker()).run_test(3)
    CrackerTester(text, MyszkowskiTranspositionCipher, MyszkowskiTranspositionCracker()).run_test(10)
    CrackerTester(text, lambda key: PlayfairCipher(key, ALPHABET_IJ_MERGED), PlayfairCracker(ALPHABET_IJ_MERGED)).run_test(3)


if __name__ == '__main__':
    main()
