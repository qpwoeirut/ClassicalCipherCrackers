import string

from ciphers.AffineCipher import AffineCipher


# the Caesar Cipher is a type of Affine Cipher
class CaesarCipher(AffineCipher):
    """
    Implementation of the Caesar cipher: https://en.wikipedia.org/wiki/Caesar_cipher
    The key is a number between 0 and the length of the alphabet
    """
    def __init__(self, rotations: int, alphabet=string.ascii_uppercase):
        super().__init__((1, rotations), alphabet=alphabet)
