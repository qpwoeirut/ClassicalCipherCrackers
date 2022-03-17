import random
import string
from math import sqrt
from sympy import Matrix, ImmutableMatrix

from ciphers.Cipher import Cipher


class HillCipher(Cipher):
    def __init__(self, key: ImmutableMatrix or str, alphabet: str = string.ascii_uppercase, safe_mode: bool = True):

        if isinstance(key, str):
            n = int(sqrt(len(key)))  # TODO replace with math.isqrt once PyPy gets to python3.8
            if safe_mode and n ** 2 != len(key):
                raise ValueError("Key length must be a perfect square")

            key = ImmutableMatrix(Matrix([[alphabet.index(key[r * n + c]) for c in range(n)] for r in range(n)]))

        if safe_mode and key.det() == 0:
            raise ValueError("Encryption matrix must be invertible (and have a nonzero determinant)")

        self.decryption_key = ImmutableMatrix(key.inv_mod(len(alphabet)))

        super().__init__(key, alphabet=alphabet)

        self.indexes = {alphabet[i]: i for i in range(len(alphabet))}

    def multiply_block(self, block: str, matrix: ImmutableMatrix):
        block_vector = ImmutableMatrix(Matrix([self.indexes[c] for c in block]))
        product_vector = (matrix * block_vector) % len(self.alphabet)
        return ''.join([self.alphabet[c] for c in product_vector])

    def encrypt(self, plaintext: str) -> str:
        if len(plaintext) % self.key.rows > 0:
            plaintext += ''.join([random.choice(self.alphabet) for _ in range(self.key.rows - (len(plaintext) % self.key.rows))])
        return ''.join([
            self.multiply_block(plaintext[i:i + self.key.rows], self.key)
            for i in range(0, len(plaintext), self.key.rows)
        ])

    def decrypt(self, ciphertext: str) -> str:
        return ''.join([
            self.multiply_block(ciphertext[i:i + self.key.rows], self.decryption_key)
            for i in range(0, len(ciphertext), self.key.rows)
        ])


if __name__ == "__main__":
    print(HillCipher("GYBNQKURP".upper()).encrypt("ACTCAT".upper()))  # POHFIN
