import abc

from ciphers.Cipher import Cipher


class Cracker(metaclass=abc.ABCMeta):
    def __init__(self, cipher: Cipher):
        self.cipher = cipher

    @abc.abstractmethod
    def crack(self, ciphertext: str) -> tuple:
        """
        Attempts to decrypt the provided ciphertext without the key
        Returns a tuple with (key, plaintext)
        """
        raise NotImplementedError()
