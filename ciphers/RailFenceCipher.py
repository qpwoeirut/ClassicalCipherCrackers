import string
from typing import Tuple

from ciphers.Cipher import Cipher
from ciphers.TranspositionCipher import TranspositionCipher


class RailFenceCipher(TranspositionCipher):
    """
    Implementation of the rail fence cipher: https://en.wikipedia.org/wiki/Rail_fence_cipher
    The key is a tuple with two integers (rails, offset), which are the number of rails and the starting offset
    The number of rails must be at least 3 and the offset cannot be more than 2 * rails - 3
    """
    def __init__(self, key: Tuple[int, int]):
        self.rails, self.offset = key
        assert self.rails >= 3
        assert self.offset <= 2 * self.rails - 3

        super().__init__(key)

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
