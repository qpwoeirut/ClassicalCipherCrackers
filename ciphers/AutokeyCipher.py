import string

from ciphers.Cipher import Cipher


class AutokeyCipher(Cipher):
    """
    Implementation of the Autokey cipher: https://en.wikipedia.org/wiki/Autokey_cipher
    The key is a string
    """
    def __init__(self, key: str, alphabet: str = string.ascii_uppercase):
        super().__init__(key, alphabet=alphabet)
        self.key_ords = [alphabet.index(k) for k in key]
        self.indexes = {alphabet[i]: i for i in range(len(alphabet))}

    def encrypt(self, plaintext: str) -> str:
        return ''.join([
            self.alphabet[(self.indexes[c] + self.indexes[k]) % len(self.alphabet)] if c in self.alphabet else c
            for k, c in zip(self.key + plaintext, plaintext)
        ])

    def decrypt(self, ciphertext: str) -> str:
        pt = ['' for _ in ciphertext]
        for i, c in enumerate(ciphertext):
            key_i = self.key_ords[i] if i < len(self.key) else self.indexes[pt[i - len(self.key)]]
            pt[i] = self.alphabet[(self.indexes[c] - key_i) % len(self.alphabet)]
        return ''.join(pt)
