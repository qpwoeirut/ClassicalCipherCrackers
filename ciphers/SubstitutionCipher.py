import string

from ciphers.Cipher import Cipher


class SubstitutionCipher(Cipher):
    def __init__(self, transformed_alphabet: str, alphabet: str = string.ascii_uppercase):
        super().__init__(transformed_alphabet, alphabet=alphabet)

        self.encryption_table = str.maketrans(self.alphabet, transformed_alphabet)
        self.decryption_table = str.maketrans(transformed_alphabet, self.alphabet)

    def encrypt(self, plaintext: str) -> str:
        plaintext = self.filter_invalid(plaintext)
        return plaintext.translate(self.encryption_table)

    def decrypt(self, ciphertext: str) -> str:
        ciphertext = self.filter_invalid(ciphertext)
        return ciphertext.translate(self.decryption_table)
