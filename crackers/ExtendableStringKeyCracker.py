import abc
import random
import string

from crackers.ClimbingCracker import ClimbingCracker
from crackers.SubstitutionCracker import SubstitutionCracker


class ExtendableStringKeyCracker(ClimbingCracker, SubstitutionCracker, metaclass=abc.ABCMeta):
    def __init__(self, alphabet: str, restart_threshold=200, iterations=5000, max_key_len=15):
        ClimbingCracker.__init__(self, restart_threshold=restart_threshold, iterations=iterations)
        SubstitutionCracker.__init__(self, alphabet=alphabet)
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
