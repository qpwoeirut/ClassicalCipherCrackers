import string
from typing import Tuple

from ciphers.Cipher import Cipher


class ColumnarTranspositionCipher(Cipher):
    """
    Implementation of the Columnar Transposition cipher: https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition
    Works for both complete columnar and incomplete columnar
    The key is a permutation starting from 0, representing the order the columns should be read off when encrypting
    """
    def __init__(self, key: Tuple[int, ...], alphabet: str = string.ascii_uppercase):
        super().__init__(key, alphabet=alphabet)
        self.inv_key = [key.index(i) for i in range(len(key))]

    def encrypt(self, plaintext: str) -> str:
        return ''.join([
            ''.join([
                plaintext[r * len(self.key) + k]
                for r in range((len(plaintext) + len(self.key) - k - 1) // len(self.key))  # ceil division
            ]) for k in self.inv_key
        ])

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ["" for _ in ciphertext]  # ceil division
        i = 0
        for c, k in enumerate(self.inv_key):
            for r in range((len(plaintext) + len(self.key) - k - 1) // len(self.key)):
                plaintext[r * len(self.key) + k] = ciphertext[i]
                i += 1
        return ''.join(plaintext)
