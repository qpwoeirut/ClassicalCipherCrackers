import string

from ciphers.AutokeyCipher import AutokeyCipher
from crackers.ExtendableStringKeyCracker import ExtendableStringKeyCracker


class AutokeyCracker(ExtendableStringKeyCracker):
    def __init__(self, alphabet=string.ascii_uppercase, restart_threshold=200, iterations=5000, max_key_len=15):
        super().__init__(AutokeyCipher, alphabet=alphabet, restart_threshold=restart_threshold, iterations=iterations,
                         max_key_len=max_key_len)

    def decrypt(self, key, ciphertext: str) -> str:
        return AutokeyCipher(key).decrypt(ciphertext)
