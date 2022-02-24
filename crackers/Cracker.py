import abc


class Cracker(metaclass=abc.ABCMeta):
    def __init__(self, alphabet: str):
        self.alphabet = alphabet

    @abc.abstractmethod
    def crack(self, ciphertext: str) -> tuple:
        """
        Attempts to decrypt the provided ciphertext without the key
        Returns a tuple with (key, plaintext)
        """
        raise NotImplementedError()
