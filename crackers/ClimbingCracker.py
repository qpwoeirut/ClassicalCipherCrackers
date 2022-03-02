import abc
import string
from typing import Type

from ciphers.Cipher import Cipher
from crackers.Cracker import Cracker
from text_fitness.quadgram_score import quadgram_score


class ClimbingCracker(Cracker):
    def __init__(self, cipher: Type[Cipher], alphabet=string.ascii_uppercase, restart_threshold=1000):
        super().__init__(cipher, alphabet)
        self.restart_threshold = restart_threshold

    @abc.abstractmethod
    def generate_random_key(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def mutate_key(self, key):
        raise NotImplementedError()

    def crack(self, ciphertext: str) -> tuple:
        best_solution = (float('-inf'), None, None)
        for i in range(10000):
            if i % 1000 == 0:
                print(f"Starting iteration {i}")

            current_key = self.generate_random_key()
            current_score = quadgram_score(self.cipher(current_key, self.alphabet).decrypt(ciphertext))

            failed_mutations = 0
            while failed_mutations < self.restart_threshold:
                mutated_key = self.mutate_key(current_key)
                mutated_plaintext = self.cipher(mutated_key, self.alphabet).decrypt(ciphertext)
                mutated_score = quadgram_score(mutated_plaintext)

                if best_solution[0] < mutated_score:
                    best_solution = (mutated_score, mutated_key, mutated_plaintext)  # TODO make sure this makes a copy
                    print(best_solution)
                if current_score < mutated_score:
                    current_score = mutated_score
                    current_key = mutated_key
                    failed_mutations = 0
                else:
                    failed_mutations += 1
        return best_solution
