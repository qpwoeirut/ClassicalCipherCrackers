import abc
from typing import Type

from ciphers.Cipher import Cipher
from crackers.Cracker import Cracker


class SubstitutionCracker(Cracker, metaclass=abc.ABCMeta):
    def __init__(self, cipher: Type[Cipher], alphabet: str):
        super().__init__(cipher)
        self.alphabet = alphabet
