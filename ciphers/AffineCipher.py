import string
from math import gcd

from ciphers.SubstitutionCipher import SubstitutionCipher


class AffineCipher(SubstitutionCipher):
    def __init__(self, key: tuple, alphabet: str = string.ascii_uppercase):
        a, b = key
        if gcd(a, len(alphabet)) != 1:
            raise ValueError(f'"a" ({a}) must be coprime with the alphabet size ({len(alphabet)})')

        # precalculate each character's encrypted and decrypted form
        transformed_alphabet = ''.join([
            alphabet[(a * alphabet.index(c) + b) % len(alphabet)]  # ax + b
            for c in alphabet
        ])
        super().__init__(transformed_alphabet=transformed_alphabet, alphabet=alphabet)


def test():
    # example from Wikipedia
    cipher = AffineCipher((5, 8))
    assert cipher.encrypt("AFFINECIPHER".lower()) == "IHHWVCSWFRCP".lower()
    assert cipher.decrypt("IHHWVCSWFRCP".lower()) == "AFFINECIPHER".lower()


def main():
    test()


if __name__ == '__main__':
    main()
