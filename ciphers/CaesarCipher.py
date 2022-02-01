import string

from ciphers.AffineCipher import AffineCipher


# the Caesar Cipher is a type of Affine Cipher
class CaesarCipher(AffineCipher):
    def __init__(self, rotations: int, alphabet=string.ascii_uppercase):
        super().__init__(a=1, b=rotations, alphabet=alphabet)


def test():
    # test from Wikipedia
    cipher = CaesarCipher(23)
    pt = cipher.filter_invalid("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
    ct = cipher.filter_invalid("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD")
    assert cipher.encrypt(pt) == ct
    assert cipher.decrypt(ct) == pt


def main():
    test()


if __name__ == '__main__':
    main()