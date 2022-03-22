import random
import string
from typing import Type

from ciphers.Cipher import Cipher
from ciphers.MonoSubstitutionCipher import MonoSubstitutionCipher
from crackers.ClimbingCracker import ClimbingCracker
from crackers.SubstitutionCracker import SubstitutionCracker


class MonoSubstitutionCracker(ClimbingCracker, SubstitutionCracker):
    def __init__(self, cipher: Type[Cipher] = MonoSubstitutionCipher, alphabet=string.ascii_uppercase,
                 restart_threshold=200, iterations=5000):
        super(ClimbingCracker).__init__(alphabet=alphabet)
        super(MonoSubstitutionCracker, self).__init__(restart_threshold=restart_threshold, iterations=iterations)
        self.cipher = cipher

    def decrypt(self, key, ciphertext: str) -> str:
        return self.cipher(key).decrypt(ciphertext)

    # TODO maybe make keys lists or tuples instead?
    def generate_random_key(self) -> str:
        letters = self.alphabet
        random.shuffle(list(letters))
        return ''.join(letters)

    def mutate_key(self, key: str) -> str:
        i1 = random.randint(0, len(key) - 1)
        i2 = random.randint(0, len(key) - 1)
        while i1 == i2:
            i2 = random.randint(0, len(key) - 1)

        if i1 > i2:
            i1, i2 = i2, i1

        return key[:i1] + key[i2] + key[i1 + 1:i2] + key[i1] + key[i2 + 1:]
