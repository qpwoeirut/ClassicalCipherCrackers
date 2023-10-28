import abc
from math import sqrt

from ciphers.SubstitutionCipher import SubstitutionCipher


class PolybiusSquareCipher(SubstitutionCipher, metaclass=abc.ABCMeta):
    """
    Abstract base class for all ciphers that use a polybius square as the key
    """
    def __init__(self, key: str, alphabet: str):
        self.size = int(sqrt(len(key)))
        assert self.size ** 2 == len(key), "Key must be a square"
        assert set(key) == set(alphabet), "Every character in the alphabet must be in the key exactly once"

        super().__init__(key)
        self.alphabet = alphabet
