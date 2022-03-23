import random
from typing import List

from ciphers.MyszkowskiTranspositionCipher import MyszkowskiTranspositionCipher
from crackers.ClimbingCracker import ClimbingCracker


# TODO this cracker is rather inefficient and needs either its mutation algorithm or climbing algorithm to be improved
class MyszkowskiTranspositionCracker(ClimbingCracker):
    def __init__(self, restart_threshold=800, iterations=1000, max_key_len=20):
        super().__init__(restart_threshold=restart_threshold, iterations=iterations)
        self.max_key_len = max_key_len

    def decrypt(self, key, ciphertext: str) -> str:
        return MyszkowskiTranspositionCipher(key).decrypt(ciphertext)

    def generate_random_key(self) -> List[int]:  # generates key of random length
        key = random.choices([0, 1, 1], k=random.randint(4, self.max_key_len))
        for i in range(1, len(key)):
            key[i] += key[i-1]
        random.shuffle(key)
        return key

    def mutate_key(self, key: List[int]) -> List[int]:
        random_index = random.randint(0 if len(key) == 1 else -1, len(key) + 1 - 2 * (len(key) == self.max_key_len))
        if random_index == -1:
            new_key = key.copy()
            new_key.remove(max(key))
            return new_key  # shortens key
        if random_index == len(key):  # extends key
            return key + [random.randint(0, len(key))]

        random_index2 = random.randint(0, len(key) - 1)
        random_index3 = random.randint(0, len(key) - 1)
        new_key = key.copy()
        new_key[random_index2], new_key[random_index3] = new_key[random_index3], new_key[random_index2]
        if len(key)*2 <= self.max_key_len and random_index == len(key) + 1:  # doubles key length
            return key + [k + len(key) for k in new_key]

        return new_key  # swaps two parts of key
