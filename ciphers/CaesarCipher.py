import string

from ciphers.AffineCipher import AffineCipher


# the Caesar Cipher is a type of Affine Cipher
class CaesarCipher(AffineCipher):
    def __init__(self, rotations: int, alphabet=string.ascii_lowercase):
        super().__init__(a=1, b=rotations, alphabet=alphabet)
