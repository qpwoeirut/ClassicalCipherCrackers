import string
from typing import Tuple

from ciphers.Cipher import Cipher


# https://en.wikipedia.org/wiki/Transposition_cipher#Columnar_transposition
class ColumnarTranspositionCipher(Cipher):
    def __init__(self, key: Tuple[int, ...], alphabet: str = string.ascii_uppercase):
        super().__init__(key, alphabet=alphabet)
        self.inv_key = [key.index(i) for i in range(len(key))]

    def encrypt(self, plaintext: str) -> str:
        return ''.join([
            ''.join([
                plaintext[r * len(self.key) + k]
                for r in range((len(plaintext) + len(self.key) - k - 1) // len(self.key))  # ceil division
            ]) for k in self.inv_key
        ])

    def decrypt(self, ciphertext: str) -> str:
        plaintext = ["" for _ in ciphertext]  # ceil division
        i = 0
        for c, k in enumerate(self.inv_key):
            for r in range((len(plaintext) + len(self.key) - k - 1) // len(self.key)):
                plaintext[r * len(self.key) + k] = ciphertext[i]
                i += 1
        return ''.join(plaintext)


def test():
    # example from Wikipedia
    cipher = ColumnarTranspositionCipher((5, 2, 1, 3, 0, 4))
    assert cipher.encrypt("WEAREDISCOVEREDFLEEATONCEQKJEU".lower()) == "EVLNEACDTKESEAQROFOJDEECUWIREE".lower()
    assert cipher.decrypt("EVLNEACDTKESEAQROFOJDEECUWIREE".lower()) == "WEAREDISCOVEREDFLEEATONCEQKJEU".lower()
    assert cipher.encrypt("WEAREDISCOVEREDFLEEATONCE".lower()) == "EVLNACDTESEAROFODEECWIREE".lower()
    assert cipher.decrypt("EVLNACDTESEAROFODEECWIREE".lower()) == "WEAREDISCOVEREDFLEEATONCE".lower()


def main():
    test()


if __name__ == '__main__':
    main()
