import string

from ciphers.BeaufortCipher import BeaufortCipher
from crackers.ExtendableStringKeyCracker import ExtendableStringKeyCracker


class BeaufortCracker(ExtendableStringKeyCracker):
    def __init__(self, alphabet=string.ascii_uppercase, restart_threshold=500, iterations=100, max_key_len=20):
        super().__init__(alphabet=alphabet, restart_threshold=restart_threshold, iterations=iterations,
                         max_key_len=max_key_len)

    def decrypt(self, key, ciphertext: str) -> str:
        return BeaufortCipher(key).decrypt(ciphertext)
