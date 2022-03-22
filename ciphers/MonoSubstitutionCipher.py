import string

from ciphers.SubstitutionCipher import SubstitutionCipher


class MonoSubstitutionCipher(SubstitutionCipher):
    """
    Implementation of a monoalphabetic substitution cipher: https://en.wikipedia.org/wiki/Substitution_cipher#Simple_substitution
    The key is the alphabet after it's encrypted
    This class serves as the base class for all monoalphabetic substitution ciphers, such as the Affine cipher
    """
    def __init__(self, transformed_alphabet: str, alphabet: str = string.ascii_uppercase):
        super().__init__(transformed_alphabet, alphabet=alphabet)

        self.encryption_table = str.maketrans(self.alphabet, transformed_alphabet)
        self.decryption_table = str.maketrans(transformed_alphabet, self.alphabet)

    def encrypt(self, plaintext: str) -> str:
        return plaintext.translate(self.encryption_table)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext.translate(self.decryption_table)
