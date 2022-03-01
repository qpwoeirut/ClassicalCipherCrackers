import random
import string

from ciphers.VigenereCipher import VigenereCipher
from crackers.ClimbingCracker import ClimbingCracker


class VigenereCracker(ClimbingCracker):
    def __init__(self, alphabet=string.ascii_uppercase, max_key_len=15):
        super().__init__(VigenereCipher, alphabet)
        self.max_key_len = max_key_len

    # TODO maybe make keys lists or tuples instead?
    def generate_random_key(self) -> str:  # generates key of random length
        key_len = random.randint(1, self.max_key_len)
        return ''.join(random.choices(string.ascii_uppercase, k=key_len))

    def mutate_key(self, key: str) -> str:
        random_index = random.randint(-(len(key) > 1), len(key))
        if random_index == -1:
            return key[:-1]
        return key[:random_index] + random.choice(string.ascii_uppercase) + key[random_index+1:]


if __name__ == '__main__':
    # the cracker finds the right answer but also finds other solutions that have a better score
    print(VigenereCracker().crack("thisisalongsentenceandhopefullyitcanbedecryptedproperly".upper()))
    print(VigenereCracker().crack(VigenereCipher("OMGHI").encrypt("hopefullythisworksifimakethetextveryverylong".upper())))
