from ciphers.PolybiusSquareCipher import PolybiusSquareCipher


class BifidCipher(PolybiusSquareCipher):
    """
    Implementation of the Bifid cipher: https://en.wikipedia.org/wiki/Bifid_cipher
    The key is a string representing 5x5 or 6x6 grid which contains all the characters in the alphabet exactly once
    Alphabet is a required parameter since the default ascii_uppercase doesn't work
    """

    def __init__(self, key: str, alphabet: str):
        super().__init__(key, alphabet=alphabet)

        self.position = {c: (i // self.size, i % self.size) for i, c in enumerate(key)}

    def encrypt(self, plaintext: str) -> str:
        idxs = [self.position[c][0] for c in plaintext] + [self.position[c][1] for c in plaintext]
        return ''.join([self.key[idxs[i] * self.size][idxs[i + 1]] for i in range(0, len(idxs), 2)])

    def decrypt(self, ciphertext: str) -> str:
        idxs = [i for sublist in [self.position[c] for c in ciphertext] for i in sublist]
        return ''.join(self.key[idxs[i] * self.size][idxs[i + len(ciphertext)]] for i in range(len(ciphertext)))
