import random
from math import sqrt

from ciphers.PlayfairCipher import PlayfairCipher
from crackers.ClimbingCracker import ClimbingCracker


class PlayfairCracker(ClimbingCracker):
    # Alphabet is a required parameter since the default ascii_uppercase doesn't work
    def __init__(self, alphabet: str, restart_threshold=500, iterations=100):
        super().__init__(restart_threshold=restart_threshold, iterations=iterations)
        self.alphabet = alphabet
        assert int(sqrt(len(self.alphabet)))**2 == len(self.alphabet), "alphabet length should be a perfect square"

    def decrypt(self, key, ciphertext: str) -> str:
        return PlayfairCipher(key, self.alphabet).decrypt(ciphertext)

    def generate_random_key(self):
        key = list(self.alphabet)
        random.shuffle(key)
        return ''.join(key)

    def mutate_key(self, key):
        random_index0 = random.randint(0, len(key - 1))
        random_index1 = random.randint(0, len(key - 1))
        new_key = key
        new_key[random_index0], new_key[random_index1] = new_key[random_index1], new_key[random_index0]
        return new_key
