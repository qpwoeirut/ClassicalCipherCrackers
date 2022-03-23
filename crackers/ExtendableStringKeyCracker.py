import abc
import random
import string

from crackers.ClimbingCracker import ClimbingCracker
from crackers.SubstitutionCracker import SubstitutionCracker


class ExtendableStringKeyCracker(ClimbingCracker, SubstitutionCracker, metaclass=abc.ABCMeta):
    def __init__(self, alphabet: str, restart_threshold: int, iterations: int, max_key_len: int):
        ClimbingCracker.__init__(self, restart_threshold=restart_threshold, iterations=iterations)
        SubstitutionCracker.__init__(self, alphabet=alphabet)
        self.max_key_len = max_key_len

    # TODO maybe make keys lists or tuples instead?
    def generate_random_key(self) -> str:  # generates key of random length
        key_len = random.randint(1, self.max_key_len)
        return ''.join(random.choices(string.ascii_uppercase, k=key_len))

    def mutate_key(self, key: str) -> str:
        random_index = random.randint(0 if len(key) == 1 else -1, len(key) - (len(key) == self.max_key_len))
        if random_index == -1:  # remove last character
            return key[:-1]
        # either replaces a character (if random_index < len(key)) or adds one to the end (if random_index == len(key))
        return key[:random_index] + random.choice(string.ascii_uppercase) + key[random_index + 1:]
