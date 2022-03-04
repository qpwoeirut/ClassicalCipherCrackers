import random
import string
from typing import Type

from ciphers.Cipher import Cipher
from crackers.ClimbingCracker import ClimbingCracker


class ExtendableStringKeyCracker(ClimbingCracker):
    def __init__(self, cipher: Type[Cipher], alphabet=string.ascii_uppercase, restart_threshold=200, iterations=5000,
                 max_key_len=15):
        super().__init__(cipher, alphabet=alphabet, restart_threshold=restart_threshold, iterations=iterations)
        self.max_key_len = max_key_len

    # TODO maybe make keys lists or tuples instead?
    def generate_random_key(self) -> str:  # generates key of random length
        key_len = random.randint(1, self.max_key_len)
        return ''.join(random.choices(string.ascii_uppercase, k=key_len))

    def mutate_key(self, key: str) -> str:
        random_index = random.randint(-(len(key) > 1), len(key))
        if random_index == -1:
            return key[:-1]
        return key[:random_index] + random.choice(string.ascii_uppercase) + key[random_index + 1:]
