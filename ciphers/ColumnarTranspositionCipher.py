from typing import Tuple, List

from ciphers.TranspositionCipher import TranspositionCipher


class ColumnarTranspositionCipher(TranspositionCipher):
    """
    Implementation of the Columnar transposition cipher: https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition
    Works for both complete columnar and incomplete columnar
    The key is a permutation starting from 0, representing the order the columns should be read off when encrypting
    """
    def __init__(self, key: Tuple[int, ...] or List[int, ...]):
        super().__init__(key)
        self.inv_key = [key.index(i) for i in range(len(key))]

    def encrypt(self, plaintext: str) -> str:
        return ''.join([
            ''.join([
                plaintext[r * len(self.key) + k]
                for r in range((len(plaintext) + len(self.key) - k - 1) // len(self.key))  # ceil division
            ]) for k in self.inv_key
        ])

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ["" for _ in ciphertext]
        i = 0
        for c, k in enumerate(self.inv_key):
            for r in range((len(plaintext) + len(self.key) - k - 1) // len(self.key)):  # ceil division
                plaintext[r * len(self.key) + k] = ciphertext[i]
                i += 1
        return ''.join(plaintext)
