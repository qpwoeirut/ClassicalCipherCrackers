import abc
import string
from sympy import ImmutableMatrix
from typing import Union, Tuple

from ciphers.Cipher import Cipher


class SubstitutionCipher(Cipher, metaclass=abc.ABCMeta):
    def __init__(self, key: Union[str, int, Tuple[int, ...], ImmutableMatrix], alphabet: str = string.ascii_uppercase):
        super().__init__(key)
        self.alphabet = alphabet

    def filter_invalid(self, text: str) -> str:
        return ''.join([c.upper() for c in text if c.upper() in self.alphabet])
