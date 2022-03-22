import string
from math import gcd
from typing import Tuple

from ciphers.MonoSubstitutionCipher import MonoSubstitutionCipher


class AffineCipher(MonoSubstitutionCipher):
    """
    Implementation of the Affine cipher: https://en.wikipedia.org/wiki/Affine_cipher
    The key is a tuple with two integers (a, b), where a is coprime with the length of the alphabet
    """
    def __init__(self, key: Tuple[int, int], alphabet: str = string.ascii_uppercase):
        a, b = key
        if gcd(a, len(alphabet)) != 1:
            raise ValueError(f'"a" ({a}) must be coprime with the alphabet size ({len(alphabet)})')

        # precalculate each character's encrypted and decrypted form
        transformed_alphabet = ''.join([
            alphabet[(a * alphabet.index(c) + b) % len(alphabet)]  # ax + b
            for c in alphabet
        ])
        super().__init__(transformed_alphabet=transformed_alphabet, alphabet=alphabet)
