import abc

from crackers.Cracker import Cracker


class SubstitutionCracker(Cracker, metaclass=abc.ABCMeta):
    def __init__(self, alphabet: str):
        super().__init__()
        self.alphabet = alphabet
