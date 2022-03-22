import abc
from typing import Type

from ciphers.Cipher import Cipher


class Cracker(metaclass=abc.ABCMeta):
    def __init__(self, cipher: Type[Cipher], alphabet: str):
        self.cipher = cipher
        self.alphabet = alphabet

    @abc.abstractmethod
    def generate_random_key(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def crack(self, ciphertext: str) -> tuple:
        """
        Attempts to decrypt the provided ciphertext without the key
        Returns a tuple with (key, plaintext)
        """
        raise NotImplementedError()

    def crack_preserve_case(self, ciphertext: str):
        is_lower = [c.islower() for c in ciphertext]
        plaintext = self.crack(ciphertext.upper())
        return ''.join([c.lower() if is_lower[i] else c for i, c in enumerate(plaintext)])
