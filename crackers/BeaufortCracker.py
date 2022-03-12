import string

from ciphers.BeaufortCipher import BeaufortCipher
from crackers.ExtendableStringKeyCracker import ExtendableStringKeyCracker


class BeaufortCracker(ExtendableStringKeyCracker):
    def __init__(self, alphabet=string.ascii_uppercase, restart_threshold=200, iterations=5000, max_key_len=15):
        super().__init__(BeaufortCipher, alphabet=alphabet, restart_threshold=restart_threshold, iterations=iterations,
                         max_key_len=max_key_len)
