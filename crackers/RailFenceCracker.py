import random
import string
from typing import Tuple

from ciphers.RailFenceCipher import RailFenceCipher
from crackers.BruteCracker import BruteCracker


class RailFenceCracker(BruteCracker):
    def __init__(self, alphabet=string.ascii_uppercase, max_rails: int = 20):
        super().__init__(RailFenceCipher, alphabet)
        self.max_rails = max_rails

    def generate_random_key(self) -> Tuple[int, int]:
        rails = random.randint(3, self.max_rails)
        offset = random.randint(0, 2 * rails - 3)
        return rails, offset

    def generate_keys(self):
        for rails in range(3, self.max_rails + 1):
            for offset in range(2 * rails - 2):
                yield rails, offset
