from typing import Tuple

from ciphers.TranspositionCipher import TranspositionCipher


class MyszkowskiTranspositionCipher(TranspositionCipher):
    """
    Implementation of the Myszkowski transposition cipher: https://en.wikipedia.org/wiki/Transposition_cipher#Myszkowski_transposition
    The key is a string or tuple, preferably with duplicate letters/numbers
    """
    def __init__(self, key: Tuple[int, ...] or str):
        if isinstance(key, str):
            key_chars = sorted(set(key))
            key = [key_chars.index(c) for c in key]

        super().__init__(key)

    # TODO both the encryption and decryption seem rather inefficient
    def encrypt(self, plaintext: str) -> str:
        ciphertext = ["" for _ in plaintext]
        rows = (len(plaintext) + len(self.key) - 1) // len(self.key)

        i = 0
        for k in range(max(self.key) + 1):
            columns = [col for col, val in enumerate(self.key) if val == k]  # find all the columns to be read
            for row in range(rows):
                for col in columns:
                    if row * len(self.key) + col >= len(plaintext):
                        break
                    ciphertext[i] = plaintext[row * len(self.key) + col]
                    i += 1
        return ''.join(ciphertext)

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ["" for _ in ciphertext]
        rows = (len(plaintext) + len(self.key) - 1) // len(self.key)

        i = 0
        for k in range(max(self.key) + 1):
            columns = [col for col, val in enumerate(self.key) if val == k]  # find all the columns to be read
            for row in range(rows):
                for col in columns:
                    if row * len(self.key) + col >= len(plaintext):
                        break
                    plaintext[row * len(self.key) + col] = ciphertext[i]
                    i += 1
        return ''.join(plaintext)
