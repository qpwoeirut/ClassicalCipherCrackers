import random
import time

from crackers.Cracker import Cracker
from crackers.VigenereCracker import VigenereCracker

random.seed(0)  # seed to ensure easy reproducibility


class CrackerTimer:
    def __init__(self, text: str, cracker: Cracker):
        self.text = text.strip()
        self.cracker = cracker
        self.start_points = [0] + [i+1 for i in range(len(self.text)) if self.text[i].isspace()] + [len(self.text)]
        if len(self.start_points) < 3:
            self.start_points = range(len(self.text))

    def pick_random_excerpt(self):
        start = random.choice(self.start_points)
        finish = random.choice(self.start_points)
        while start == finish:
            finish = random.choice(self.start_points)
        return self.text[start:finish].strip().upper()

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
            assert decrypted[i][1] == keys[i]
            assert decrypted[i][2] == plaintexts[i]

        return finish - start


def main():
    with open("rabbitsign_faq.txt") as f:
        text = f.read().strip()
    CrackerTimer(text, VigenereCracker()).run_test(10)


if __name__ == '__main__':
    main()
