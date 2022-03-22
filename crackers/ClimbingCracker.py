import abc
from typing import Type

from ciphers.Cipher import Cipher
from crackers.Cracker import Cracker
from text_fitness.quadgram_score import quadgram_score


class ClimbingCracker(Cracker):
    def __init__(self, restart_threshold=100, iterations=5000):
        super().__init__()
        self.restart_threshold = restart_threshold
        self.iterations = iterations

    @abc.abstractmethod
    def generate_random_key(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def mutate_key(self, key):
        raise NotImplementedError()

    def crack(self, ciphertext: str) -> tuple:
        best_solution = (float('-inf'), None, None)
        for i in range(self.iterations):
            if i % 100 == 0:
                print(f"Starting iteration {i}")

            current_key = self.generate_random_key()
            current_score = quadgram_score(self.decrypt(current_key, ciphertext))

            failed_mutations = 0
            while failed_mutations < self.restart_threshold:
                mutated_key = self.mutate_key(current_key)
                mutated_plaintext = self.decrypt(mutated_key, ciphertext)
                mutated_score = quadgram_score(mutated_plaintext)

                if best_solution[0] < mutated_score:
                    best_solution = (mutated_score, mutated_key, mutated_plaintext)
                    print(best_solution)
                if current_score < mutated_score:
                    current_score = mutated_score
                    current_key = mutated_key
                    failed_mutations = 0
                else:
                    failed_mutations += 1
        return best_solution
