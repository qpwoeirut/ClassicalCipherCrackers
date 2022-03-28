from math import sqrt

from ciphers.SubstitutionCipher import SubstitutionCipher


class PlayfairCipher(SubstitutionCipher):
    """
    Implementation of the Playfair cipher: https://en.wikipedia.org/wiki/Playfair_cipher
    The key is a string representing 5x5 or 6x6 grid which contains all the characters in the alphabet exactly once
    Alphabet is a required parameter since the default ascii_uppercase doesn't work
    """

    def __init__(self, key: str, alphabet: str):
        size = int(sqrt(len(key)))
        assert size ** 2 == len(key), "Key must be a square"
        assert set(key) == set(alphabet), "Every character in the alphabet must be in the key exactly once"

        super().__init__(key, alphabet=alphabet)

        self.table = dict()
        for r0 in range(size):
            for c0 in range(size):
                for r1 in range(r0 + 1, size):
                    for c1 in range(c0 + 1, size):
                        bigram0 = key[r0 * size + c0] + key[r1 * size + c1]
                        if r0 == r1:
                            bigram1 = key[r0 * size + ((c0 + 1) % size)] + key[r0 * size + ((c1 + 1) % size)]
                        elif c0 == c1:
                            bigram1 = key[((r0 + 1) % size) * size + c0] + key[((r1 + 1) % size) * size + c1]
                        else:
                            bigram1 = key[r0 * size + c1] + key[r1 * size + c0]

                        self.table[bigram0] = bigram1
                        self.table[bigram0[::-1]] = bigram1[::-1]
                        self.table[bigram1] = bigram0
                        self.table[bigram1[::-1]] = bigram0[::-1]

        for r in range(size):
            for c0 in range(size):
                for c1 in range(c0 + 1, size):
                    bigram0 = key[r * size + c0] + key[r * size + c1]
                    bigram1 = key[r * size + ((c0 + 1) % size)] + key[r * size + ((c1 + 1) % size)]

                    self.table[bigram0] = bigram1
                    self.table[bigram0[::-1]] = bigram1[::-1]

        for r0 in range(size):
            for r1 in range(r0 + 1, size):
                for c in range(size):
                    bigram0 = key[r0 * size + c] + key[r1 * size + c]
                    bigram1 = key[((r0 + 1) % size) * size + c] + key[((r1 + 1) % size) * size + c]

                    self.table[bigram0] = bigram1
                    self.table[bigram0[::-1]] = bigram1[::-1]

        self.inv_table = {v: k for k, v in self.table.items()}

    # assumes there are no repeat letters; an X or Q is usually placed between repeat letters
    def encrypt(self, plaintext: str) -> str:
        assert len(plaintext) % 2 == 0
        return ''.join([self.table[plaintext[i:i + 2]] for i in range(0, len(plaintext), 2)])

    def decrypt(self, ciphertext: str) -> str:
        assert len(ciphertext) % 2 == 0
        return ''.join([self.inv_table[ciphertext[i:i + 2]] for i in range(0, len(ciphertext), 2)])
