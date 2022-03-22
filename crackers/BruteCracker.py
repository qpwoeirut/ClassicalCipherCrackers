import abc
from crackers.Cracker import Cracker
from text_fitness.quadgram_score import quadgram_score


class BruteCracker(Cracker):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def generate_keys(self):
        """
        Returns a generator with all possible keys in the keyspace
        """
        raise NotImplementedError()

    def crack(self, ciphertext: str) -> tuple:
        solutions = []
        for key in self.generate_keys():
            plaintext = self.decrypt(key, ciphertext)
            solutions.append((quadgram_score(plaintext), key, plaintext))
        solutions.sort(reverse=True)
        return solutions[0]
