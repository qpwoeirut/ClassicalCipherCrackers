import string
from itertools import cycle

from ciphers.Cipher import Cipher


class BeaufortCipher(Cipher):
    """
    Implementation of the Beaufort cipher: https://en.wikipedia.org/wiki/Beaufort_cipher
    The key is a string
    Not to be confused with the "variant Beaufort" cipher, (a Vigenere cipher where encryption/decryption are swapped)
    """
    def __init__(self, key: str, alphabet: str = string.ascii_uppercase):
        super().__init__(key, alphabet=alphabet)
        self.key_ords = [alphabet.index(k) for k in key]
        self.indexes = {alphabet[i]: i for i in range(len(alphabet))}

    def encrypt(self, plaintext: str) -> str:
        return self.decrypt(plaintext)  # the Beaufort cipher is reciprocal; encryption and decryption are the same

    def decrypt(self, ciphertext: str) -> str:
        return ''.join([
            self.alphabet[(k - self.indexes[c]) % len(self.alphabet)] if c in self.alphabet else c
            for k, c in zip(cycle(self.key_ords), ciphertext)
        ])
