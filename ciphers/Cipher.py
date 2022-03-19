import abc
import string
from typing import Union, Tuple

from sympy import ImmutableMatrix


class Cipher(metaclass=abc.ABCMeta):
    # the key parameter is unused, but having it makes each of the subclasses have a matching __init__ signature
    def __init__(self, key: Union[str, int, Tuple[int, int], ImmutableMatrix], alphabet: str = string.ascii_uppercase):
        self.key = key
        self.alphabet = alphabet

    def filter_invalid(self, text: str) -> str:
        return ''.join([c.upper() for c in text if c.upper() in self.alphabet])

    def valid_text(self, text: str) -> bool:
        return len(self.filter_invalid(text)) == len(text)

    @abc.abstractmethod
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts plaintext using the implemented cipher
        Ignores any characters not in self.alphabet
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts ciphertext using the implemented cipher
        Ignores any characters not in self.alphabet
        """
        raise NotImplementedError()
