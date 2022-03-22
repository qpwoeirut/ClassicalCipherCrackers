import string
from itertools import cycle

from ciphers.Cipher import Cipher


class VigenereCipher(Cipher):
    """
    Implementation of the Vigenère cipher: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
    The key is a string
    """
    def __init__(self, key: str, alphabet: str = string.ascii_uppercase):
        super().__init__(key, alphabet=alphabet)
        self.key_ords = [alphabet.index(k) for k in key]
        self.indexes = {alphabet[i]: i for i in range(len(alphabet))}

    def encrypt(self, plaintext: str) -> str:
        return ''.join([
            self.alphabet[(self.indexes[c] + k) % len(self.alphabet)] if c in self.alphabet else c
            for k, c in zip(cycle(self.key_ords), plaintext)
        ])

    def decrypt(self, ciphertext: str) -> str:
        return ''.join([
            self.alphabet[(self.indexes[c] - k) % len(self.alphabet)] if c in self.alphabet else c
            for k, c in zip(cycle(self.key_ords), ciphertext)
        ])
