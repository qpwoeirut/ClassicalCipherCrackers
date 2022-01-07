from math import log2


def ngram_to_number(ngram: str) -> int:
    """
    Assumes all letters are capitalized
    """
    number = 0
    for char in ngram:
        number = number * 26 + ord(char) - ord('A')
    return number


def generate_log_probabilities() -> None:
    """
    Converts the ngram frequency files into files which have an array of each ngram's log probability
    Each ngram is converted into a number using base 26
    Frequency files are from http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
    """
    for size, ngram in enumerate(("monogram", "bigram", "trigram", "quadgram")):
        with open(f"text_fitness/ngram_frequency/english_{ngram}s.txt") as file:
            ngram_frequency = {line.split()[0]: int(line.split()[1]) for line in file}

        log_total_ngrams = log2(sum(ngram_frequency.values()))
        log_probabilities = [-log_total_ngrams for _ in range(26**(size + 1))]
        for k, v in ngram_frequency.items():
            log_probabilities[ngram_to_number(k)] = log2(v) - log_total_ngrams

        with open(f"text_fitness/log_probabilities/english_{ngram}s.txt", "w") as file:
            file.write(' '.join([str(x) for x in log_probabilities]))


def main():
    generate_log_probabilities()


if __name__ == '__main__':
    main()
