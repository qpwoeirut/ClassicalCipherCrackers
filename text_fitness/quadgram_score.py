from timeit import timeit
from text_fitness.log_probabilities.generate_log_probabilities import ngram_to_number

with open("/Users/qpwoeirut/OtherProgramming/ClassicalCipherCrackers/text_fitness/log_probabilities/english_quadgrams.txt") as file:
    quadgram_prob = [float(x) for x in file.read().split()]
assert len(quadgram_prob) == 26 ** 4, \
    f"There should be 26^4 quadgrams but instead there are {len(quadgram_prob)} quadgrams."


# version 1
# uses a running quadgram number
def quadgram_score_v1(text: str) -> float:
    score = 0
    current_quadgram_number = 0
    for i in range(len(text)):
        current_quadgram_number = (current_quadgram_number * 26 + ord(text[i]) - ord('A')) % len(quadgram_prob)
        if i >= 3:
            score += quadgram_prob[current_quadgram_number]
    return score / len(text)


# version 2
def quadgram_score_v2(text: str) -> float:
    score = 0
    for i in range(3, len(text)):
        score += quadgram_prob[ngram_to_number(text[i-3:i+1])]
    return score / len(text)


# version 3
# uses formula for quadgrams
def quadgram_score_v3(text: str) -> float:
    score = 0
    for i in range(3, len(text)):
        score += quadgram_prob[
            (((ord(text[i-3]) - ord('A')) * 26 +
              ord(text[i-2]) - ord('A')) * 26 +
             ord(text[i-1]) - ord('A')) * 26 +
            ord(text[i]) - ord('A')
        ]
    return score / len(text)


# version 4
# replaces ord('A') with 65 and then extracts it out to the end
def quadgram_score_v4(text: str) -> float:
    score = 0
    for i in range(3, len(text)):
        score += quadgram_prob[
            ((ord(text[i-3]) * 26 + ord(text[i-2])) * 26 + ord(text[i-1])) * 26 + ord(text[i]) - 1188135
            # 1188135 = 1142440 + 43940 + 1690 + 65 = 65 * 26^3  +  65 * 26^2  +  65 * 26  +  65
        ]
    return score / len(text)


# version 5
# hardcodes powers of 26
def quadgram_score_v5(text: str) -> float:
    score = 0
    for i in range(3, len(text)):
        score += quadgram_prob[
            ord(text[i-3]) * 17576 + ord(text[i-2]) * 676 + ord(text[i-1]) * 26 + ord(text[i]) - 1188135
            # 1188135 = 1142440 + 43940 + 1690 + 65 = 65 * 26^3  +  65 * 26^2  +  65 * 26  +  65
        ]
    return score / len(text)


# on Stanley's computer, v4 runs slightly faster than v3 and v5, all of which run much faster than v1 and v2
quadgram_score = quadgram_score_v4


def run_timed_tests(f):
    f("faiuwehgiuaohgoiuhrgiuoheriukbnvkzjdbjseilurbgdjzfbdjsjdfbohuaehrguoaehrpguvahuihvbajkfbrbeuihruighiurhvjksgrhguierhbjk".upper())
    f("jaiowezznnzxnvxdrtfyguftdrsextdfcgznviweoiprjhguerhguherwgpuh".upper())
    f("thisshouldhaveagoodquadgramscoreanditdoes".upper())
    f("tion".upper())


def main():
    for f in [quadgram_score_v1, quadgram_score_v2, quadgram_score_v3, quadgram_score_v4, quadgram_score_v5]:
        print(timeit(lambda: run_timed_tests(f), number=1000000))


if __name__ == '__main__':
    main()
