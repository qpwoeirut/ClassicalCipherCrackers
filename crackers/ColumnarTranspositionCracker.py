import random
from typing import List

from ciphers.ColumnarTranspositionCipher import ColumnarTranspositionCipher
from crackers.ClimbingCracker import ClimbingCracker


class ColumnarTranspositionCracker(ClimbingCracker):
    def __init__(self, restart_threshold=400, iterations=800, max_key_len=20):
        super().__init__(restart_threshold=restart_threshold, iterations=iterations)
        self.max_key_len = max_key_len

    def decrypt(self, key, ciphertext: str) -> str:
        return ColumnarTranspositionCipher(key).decrypt(ciphertext)

    def generate_random_key(self) -> List[int]:  # generates key of random length
        permutation = list(range(random.randint(1, self.max_key_len)))
        random.shuffle(permutation)
        return permutation

    def mutate_key(self, key: List[int]) -> List[int]:
        random_index = random.randint(0 if len(key) == 1 else -1, len(key) + 1 - 2 * (len(key) == self.max_key_len))
        if random_index == -1:
            return [k for k in key if k != len(key) - 1]  # shortens key
        if random_index == len(key):  # extends key
            return key + [len(key)]

        random_index2 = random.randint(0, len(key) - 1)
        random_index3 = random.randint(0, len(key) - 1)
        new_key = key.copy()
        new_key[random_index2], new_key[random_index3] = new_key[random_index3], new_key[random_index2]
        if len(key) * 2 <= self.max_key_len and random_index == len(key) + 1:  # doubles key length
            offset = max(key) + 1
            return key + [k + offset for k in new_key]

        return new_key  # swaps two parts of key
