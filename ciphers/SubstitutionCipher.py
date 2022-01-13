import string

from ciphers.Cipher import Cipher


class SubstitutionCipher(Cipher):
    def __init__(self, transformed_alphabet, alphabet=string.ascii_lowercase):
        super().__init__(alphabet=alphabet)

        self.transformed_alphabet = transformed_alphabet
        self.encryption_table = str.maketrans(self.alphabet, self.transformed_alphabet)
        self.decryption_table = str.maketrans(self.transformed_alphabet, self.alphabet)

    def encrypt(self, plaintext: str) -> str:
        return plaintext.translate(self.encryption_table)

    def decrypt(self, ciphertext: str) -> str:
        return ciphertext.translate(self.decryption_table)
