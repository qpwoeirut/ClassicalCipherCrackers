import string
from math import gcd

from Cipher import Cipher


class AffineCipher(Cipher):
    def __init__(self, a: int, b: int, alphabet=string.ascii_lowercase):
        super().__init__((a, b), alphabet=alphabet)
        if gcd(a, len(self.alphabet)) != 1:
            raise ValueError(f'"a" ({a}) must be coprime with the alphabet size ({len(self.alphabet)})')

        # precalculate each character's encrypted and decrypted form
        self.transformed_alphabet = ''.join([self.encrypt_char(c) for c in self.alphabet])
        self.encryption_table = str.maketrans(self.alphabet, self.transformed_alphabet)
        self.decryption_table = str.maketrans(self.transformed_alphabet, self.alphabet)

    def encrypt_char(self, c: str) -> str:
        # enc = ax + b
        return self.alphabet[(self.key[0] * self.alphabet.index(c) + self.key[1]) % len(self.alphabet)]

    def encrypt(self, plaintext: str) -> str:
        return plaintext.translate(self.encryption_table)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext.translate(self.decryption_table)


def test():
    # example from Wikipedia
    cipher = AffineCipher(5, 8)
    assert cipher.encrypt("AFFINECIPHER".lower()) == "IHHWVCSWFRCP".lower()
    assert cipher.decrypt("IHHWVCSWFRCP".lower()) == "AFFINECIPHER".lower()


def main():
    test()


if __name__ == '__main__':
    main()
