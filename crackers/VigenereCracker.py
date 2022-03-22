import string

from ciphers.VigenereCipher import VigenereCipher
from crackers.ExtendableStringKeyCracker import ExtendableStringKeyCracker


class VigenereCracker(ExtendableStringKeyCracker):
    def __init__(self, alphabet=string.ascii_uppercase, restart_threshold=200, iterations=5000, max_key_len=15):
        super().__init__(VigenereCipher, alphabet=alphabet, restart_threshold=restart_threshold, iterations=iterations,
                         max_key_len=max_key_len)

    def decrypt(self, key, ciphertext: str) -> str:
        return VigenereCipher(key).decrypt(ciphertext)
