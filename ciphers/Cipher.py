import abc


class Cipher(metaclass=abc.ABCMeta):
    def __init__(self, alphabet: str):
        self.alphabet = alphabet

    def filter_invalid(self, text: str) -> str:
        return ''.join([c.lower() for c in text if self.valid_char(c.lower())])

    def valid_text(self, text: str) -> bool:
        return len(self.filter_invalid(text)) == len(text)

    def valid_char(self, c: str) -> bool:
        return c in self.alphabet

    @abc.abstractmethod
    def encrypt(self, plaintext: str) -> str:
        """
        Encrypts plaintext using the implemented cipher
        Assumes plaintext is valid (all chars are in self.alphabet)
        """
        raise NotImplementedError()

    @abc.abstractmethod
    def decrypt(self, ciphertext: str) -> str:
        """
        Decrypts ciphertext using the implemented cipher
        Assumes ciphertext is valid (all chars are in self.alphabet)
        """
        raise NotImplementedError()
