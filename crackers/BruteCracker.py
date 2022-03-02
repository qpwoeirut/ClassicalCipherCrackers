import abc
import string
from typing import Type

from ciphers.Cipher import Cipher
from crackers.Cracker import Cracker
from text_fitness.quadgram_score import quadgram_score


class BruteCracker(Cracker):
    def __init__(self, cipher: Type[Cipher], alphabet=string.ascii_uppercase):
        super().__init__(cipher, alphabet)

    @abc.abstractmethod
    def generate_keys(self):
        """
        Returns a generator with all possible keys in the keyspace
        """
        raise NotImplementedError()

    def crack(self, ciphertext: str) -> tuple:
        solutions = []
        for key in self.generate_keys():
            plaintext = self.cipher(key, self.alphabet).decrypt(ciphertext)
            solutions.append((quadgram_score(plaintext), key, plaintext))
        solutions.sort(reverse=True)
        return solutions[0]
