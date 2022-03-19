import string
from typing import Tuple

from ciphers.Cipher import Cipher


class RailFenceCipher(Cipher):
    def __init__(self, key: Tuple[int, int], alphabet: str = string.ascii_uppercase):
        self.rails, self.offset = key
        assert self.rails >= 3
        assert self.offset <= 2 * self.rails - 3

        super().__init__(key, alphabet=alphabet)

    def _fence(self, s: list or str) -> list:
        fence = [[None] * len(s) for _ in range(self.rails)]
        if self.offset < self.rails:
            rails = [*range(self.offset, self.rails - 1)] + [*range(self.rails - 1, 0, -1)] + [*range(self.offset)]
        else:
            rails = [*range(self.offset, 0, -1)] + [*range(self.rails)] + [*range(self.rails - 1, self.offset, -1)]

        for i, x in enumerate(s):
            fence[rails[i % len(rails)]][i] = x

        return [c for rail in fence for c in rail if c is not None]

    def encrypt(self, plaintext: str) -> str:
        return ''.join(self._fence(plaintext))

    def decrypt(self, ciphertext: str) -> str:
        nums = list(range(len(ciphertext)))
        pos = self._fence(nums)
        return ''.join(ciphertext[pos.index(n)] for n in nums)


if __name__ == "__main__":
    cipher = RailFenceCipher((4, 3))
    assert cipher.encrypt("abcdefghijklmnop") == "djpceikobfhlnagm"
    assert cipher.decrypt("djpceikobfhlnagm") == "abcdefghijklmnop"
    assert RailFenceCipher((3, 0)).encrypt("WEAREDISCOVEREDRUNATONCE") == "WECRUOERDSOEERNTNEAIVDAC"
    assert RailFenceCipher((3, 0)).decrypt("WECRUOERDSOEERNTNEAIVDAC") == "WEAREDISCOVEREDRUNATONCE"
