import random
import time

from crackers.Cracker import Cracker
from crackers.VigenereCracker import VigenereCracker

random.seed(0)  # seed to ensure easy reproducibility


class CrackerTester:
    def __init__(self, text: str, cracker: Cracker):
        self.cracker = cracker
        self.text = self.cracker.cipher("", alphabet=cracker.alphabet).filter_invalid(text.strip())

    def pick_random_excerpt(self):
        a = random.choice(range(len(self.text)))
        b = random.choice(range(len(self.text)))
        while a == b:
            b = random.choice(range(len(self.text)))

        return self.text[min(a, b):max(a, b)].strip().upper()

    def run_test(self, trials: int) -> float:
        plaintexts = [self.pick_random_excerpt() for _ in range(trials)]
        keys = [self.cracker.generate_random_key() for _ in range(trials)]
        ciphertexts = [self.cracker.cipher(keys[i]).encrypt(plaintexts[i]) for i in range(trials)]
        print(plaintexts)
        print(keys)
        print(ciphertexts)

        start = time.time()
        decrypted = [self.cracker.crack(ciphertext) for ciphertext in ciphertexts]
        finish = time.time()

        for i in range(trials):
            assert decrypted[i][2] == plaintexts[i], f"\n{decrypted[i][2]}\n{plaintexts[i]}"
            assert self.keys_match(decrypted[i][1], keys[i]), f"\n{decrypted[i][1]}\n{keys[i]}"

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
    CrackerTester(text, VigenereCracker(iterations=300)).run_test(8)


if __name__ == '__main__':
    main()
