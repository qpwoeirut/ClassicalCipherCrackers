import abc
from sympy import ImmutableMatrix
from typing import Union, Tuple

from ciphers.Cipher import Cipher


class TranspositionCipher(Cipher, metaclass=abc.ABCMeta):
    def __init__(self, key: Union[str, int, Tuple[int, ...], ImmutableMatrix]):
        super().__init__(key)

    def filter_invalid(self, text: str) -> str:
        return text
