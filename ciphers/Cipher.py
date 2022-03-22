import abc
from typing import Union, Tuple

from sympy import ImmutableMatrix


class Cipher(metaclass=abc.ABCMeta):
    """
    Abstract base class for all Cipher classes
    """
    def __init__(self, key: Union[str, int, Tuple[int, ...], ImmutableMatrix]):
        self.key = key

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

    @abc.abstractmethod
    def filter_invalid(self, text: str) -> str:
        """
        For substitution ciphers, removes any characters that are not in the alphabet
        Does nothing for all other ciphers
        """
        raise NotImplementedError()
