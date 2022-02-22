# ====================================================================================================
# Mono-alphabetic Substitution Cipher Solver Attempt 7
# --------------------------------------------------
# APPROACH
#   - Create a hashmap of all english words with a certain pattern (ex: "the" has pattern abc and
#     "status" has pattern abcbde)
#   - For each word in the cipher text, get words with its matching word pattern (ex: "hkz" has
#     the same word pattern as "the", "cat", "pad", etc)
#   - For each of the matching words found in the previous step, create a partial key using those
#     letters. The format of a partial key is a hashmap with keys a-z and values as lists of the
#     possible letter(s) that map to the key (ex: "abc" with matching word "cat" -> {"a": ["c"],
#     "b": ["a"], "c": ["t"]})
#   - Create partial key hashmaps for each of the matching words for each of the encrypted words
#   - Merge all of the possible keys using an algorithm that considers the following steps:
#       1) Take the first two maps of the list of maps passed in
#       2) To merge these two together loop through each of the letters of the alphabet (keys of the
#          maps)
#           a) Check if the possible cipher letters for a given position are unknown (the value is []).
#              If so, merge the two together (ex: [] + [a, z, t] = [a, z, t])
#           b) If both maps have possible letters in that position, find all the letters that are in
#              common between the two maps and add those, discard any letters that only appear in
#              one of the maps and not both
#       3) Use the merged map just created at one of the two maps in the next step. Continue the
#          algorithm until all of the given maps have been merged into one
#   - Clean the merged mapping by finding all of the known letters (where the list value in the merged
#     map only has 1 possible letter). For the rest of thel list values, remove all of those known
#     letters, preventing them from being using in that position
#       - NOTE: Because this algorithm may remove such that only 1 letter remains in another position,
#         it must be run multiple times (ex: {a: [z], b: [z, c], c: [c, d, f]}. The first pass would
#         result in {a: [z], b: [c], c: [c, d, f]}, but now b=c is also known so it must be run
#         again to finally get {a: [z], b: [c], c: [d, f]})
#   - Finally create a key from the cleaned and merged mapping. If a list value only has 1 letter, then
#     insert it into the key at the correct position. Otherwise, use an UNKNOWN_CHAR since there is
#     no definite answer for that position
# end: APPROACH
# ====================================================================================================


import sys
from typing import Final


ALPHABET: Final = "abcdefghijklmnopqrstuvwxyz"
UNKNOWN_CHAR: Final = "_"
english_dictionary: list = []
words_by_patterns: dict = {}


# ====================================================================================================
# def clean_cipher_text
#
# Cleans up an inputed string of cipher text by removing any characters that are not a <SPACE> or
# part of ALPHABET
#
# Arguments--
#
# encrypted_text:	the text to clean up
#
# Returns--
#
# The cleaned text without any extra characters
#
def clean_cipher_text(encrypted_text: str) -> str:
    cleaned_text: str = ""

    for char in encrypted_text.lower():
        if (char in ALPHABET + " "):
            cleaned_text += char

    return cleaned_text
# end: def clean_cipher_text


# ====================================================================================================
# def create_word_pattern
#
# Based on source: https://stackoverflow.com/questions/42125644/matching-words-to-a-pattern-in-python
# Creates a pattern of letters based on the letters of an input word (ex: "cat" -> "abc", "bee" -> "abb")
#
# Arguments--
#
# word:	the word to create a pattern for
#
# Returns--
#
# A string representing the pattern of the input word as characters of ALPHABET
#
def create_word_pattern(word: str) -> str:
    assert len(set(word)) <= len(ALPHABET), "ERR -- create_word_pattern: word has more characters than ALPHABET"

    pattern_mapping: dict = {}
    pattern_letters_left: list = list(ALPHABET)[::-1]
    pattern: list = []

    for letter in word.lower():
        if (letter not in ALPHABET):
            print(f"WARN -- create_word_pattern: letter {letter} not in ALPHABET, ignoring")
            continue
        
        if letter not in pattern_mapping:
            pattern_mapping[letter] = pattern_letters_left.pop()
        pattern.append(pattern_mapping[letter])

    return "".join(pattern)
# end: def create_word_pattern


# ====================================================================================================
# def init_word_patterns
#
# Initializes a hashmap of all the words in english_words.txt sorted by their respective word pattern
#
def init_word_patterns():
    # English words source: https://github.com/first20hours/google-10000-english/blob/master/20k.txt
    with open("english_words.txt") as eng_dict:
        global english_dictionary;
        english_dictionary = [str(x) for x in eng_dict.read().split("\n")]

    # For each word in the english words text file, determine its word pattern, then add it to a list of
    # all english words by their patterns where the key is the word pattern string and the value is a list
    # of words with that pattern
    for word in english_dictionary:
        word = word.lower()
        word_pattern: str = create_word_pattern(word)

        words: list = words_by_patterns.get(word_pattern, [])
        words.append(word)
        words_by_patterns[word_pattern] = words
# end: def init_word_patterns


# ====================================================================================================
# def get_matching_words
#
# Get a list of words with the same word pattern as the input word
#
# Arguments--
#
# word:	the word to get a list of words with the same letter pattern
#
# Returns--
#
# A list of english words with the same pattern as word
#
def get_matching_words(word: str) -> list:
    pattern: str = create_word_pattern(word)

    if (not pattern in words_by_patterns):
        return []
    return words_by_patterns[pattern]
# end: def get_matching_words


# ====================================================================================================
# def decrypt_with_key
#
# Decrypt a given encrypted_text with a given key
#
# Arguments--
#
# key:				a string with the same length as ALPHABET which represents a mapping between the
#					cipher and English letters. The position (0-26, or a-z) within the key represents
#					the cipher letter and the letters making up the key represent the associated English
#					letters ex: a key starting with "ztb..." means replace all A's with Z, all B's with T,
#					all C's with B, etc
#
# encrypted_text:	the text to decrypt with the given key
#
# Returns--
#
# encrypted_text decrypted with key
#
def decrypt_with_key(key: str, encrypted_text: str) -> str:
    assert len(key) == len(ALPHABET), f"ERR -- decrypt_with_key: key should have {len(ALPHABET)} letters"
    
    # Create a lookup table between the alphabet letters and the encrypted chars
    key_dict: dict = {}
    for i in range(len(ALPHABET)):
         key_dict[ALPHABET[i]] = key[i]

    decrypted_text: str = ""

    # Decrypt the text
    # If the char is not in the alphabet (eg puncuation), ignore it and add as it is
    # If the char is in key_dict then decrypt with the key, otherwise replace that character with
    # UNKNOWN_CHAR
    for encrypted_char in encrypted_text:
        if (encrypted_char not in ALPHABET):
            decrypted_text += encrypted_char
        else:
            try:
                decrypted_text += key_dict[encrypted_char]
            except KeyError:
                decrypted_text += UNKNOWN_CHAR
    return decrypted_text
# end: def decrypt_with_key


# ====================================================================================================
# def merge_possible_hashmaps
#
# Merges together possible mappings of encrypted and english letters
#
# Arguments--
#
# hashmaps:	a list of possible mappings. Each mapping is a hashmap with keys as letters of
#		    ALPHABET (a-z) and values as lists of the possible english letters that map to those
#			cipher letters
#
# Returns--
#
# A single mapping representing the merged product of all the mappings in hashmaps. For more
# information about how the merge works, see the APPROACH section at the top of this file
# 
def merge_possible_hashmaps(hashmaps: list) -> dict:
    fully_merged: dict = {k: [] for k in ALPHABET}

    # Loop through each of the mappings. Merge the given mapping with the master/so-far mapping "fully_merged".
    # Follow a couple of steps when deciding how to merge:
    # 	1) If the list of possible letters in either fully_merged or the hashmap being merged is empty (== []),
    #	   then just add the two together (eg, use whatever there is because there will be no conflict between
    #	   letters)
    #	2) If the lists mentioned above are both not empty, add any letters they have in common to fully_merged.
    #	   If one has a letter that the other doesn't, discard it
    for hashmap in hashmaps:
        merge_step: dict = {k: [] for k in ALPHABET}
        for l in ALPHABET:
            # Step 1
            if (hashmap[l] == [] or fully_merged[l] == []):
                merge_step[l] = list(set(fully_merged[l] + hashmap[l]))
                continue
            # Step 2
            for possible_letter in hashmap[l]:
                if possible_letter in fully_merged[l]:
                    merge_step[l] = list(set(merge_step[l] + [possible_letter]))
        fully_merged = merge_step # Continuously add back to fully_merged so everything merges to the same place

    return fully_merged
# end: def merge_possible_hashmaps


# ====================================================================================================
# def get_possible_letters
#
# Get a mapping of the encrypted letters and their possible answers as english letters
#
# Arguments--
#
# encrypted_text:	the encrypted message to get the possible keys/english letter mapping for
#
# Returns--
#
# A hashmap with keys representing the encrypted letters and values representing the possible letter(s)
# for the given encrypted letter
#
def get_possible_letters(encrypted_text: str) -> dict:
    possible_letter_maps: list = []

    # Get a single mapping
    # ----------
    # Loop through each of the encrypted words in encrypted_text and get all of the english words
    # with matching word patterns. Create a mapping for all of the matching words for all of the encrypted
    # words given the letters of the encrypted/matching word (ex: enc word "hkz" with match "cat" ->
    # {h: [c], k: [a], z: [t]}). Once all of these mappings are made, merge them together using the
    # merge_possible_hashmaps function
    for encrypted_word in encrypted_text.split():
        possible_letters: dict = {k: [] for k in ALPHABET}
        possible_words: list = get_matching_words(encrypted_word)
        for possible_word in possible_words:
            # Add all the letters in possible_word to their respective matchings in possible_letters to create
            # the mapping
            for l in range(len(encrypted_word)):
                encrypted_letter: str = encrypted_word[l]
                possible_letter: str = possible_word[l]
                possible_letters[encrypted_letter] = list(set(possible_letters[encrypted_letter] + [possible_letter]))
        possible_letter_maps.append(possible_letters)
        
    all_possible_letters: dict = merge_possible_hashmaps(possible_letter_maps)

    # Loop through all of the possibilities in all_possible_letters and remove any duplicates for the known letters.
    # Because this algorithm may remove such that only 1 letter remains in another position, it must be run multiple
    # times (ex: {a: [z], b: [z, c], c: [c, d, f]}. The first pass would result in {a: [z], b: [c], c: [c, d, f]},
    # but now b=c is also known so it must be run again to finally get {a: [z], b: [c], c: [d, f]})
    known_letters: list = []
    known_letters_left: bool = True
    while (known_letters_left):
        known_letters_left = False

        # Find all of the known letters
        for encrypted_letter in ALPHABET:
            if (len(all_possible_letters[encrypted_letter]) == 1):
                known_letters.extend(all_possible_letters[encrypted_letter])
        # Remove known letters from all other places
        for encrypted_letter in ALPHABET:
            for known_letter in known_letters:
                possible_letters: list = all_possible_letters[encrypted_letter]
                if (len(possible_letters) != 1 and known_letter in possible_letters):
                    all_possible_letters[encrypted_letter].remove(known_letter) # Known letter cannot be in another spot
                    if (len(all_possible_letters[encrypted_letter]) == 1):
                        known_letters_left = True
    
    return all_possible_letters
# end: def get_possible_letters


# ====================================================================================================
# def solve
#
# Decrypt a given string of encrypted text
#
# Arguments--
#
# encrypted_text:	the text to decrypt
#
# Returns--
#
# The decrypted text and the final key it was decrypted with
#
def solve(encrypted_text: str):
    possible_letters: dict = get_possible_letters(encrypted_text)
    key = UNKNOWN_CHAR * len(ALPHABET)

    # Given the list of possible mappings to a given cipher letter, create a final key. If there is
    # only one possible mapping, use that in the final key. Otherwise, ignore that mapping
    for encrypted_letter in ALPHABET:
        if (len(possible_letters[encrypted_letter]) == 1):
            key_index: int = ord(encrypted_letter) - 97
            key_letter: str = possible_letters[encrypted_letter][0]
            key = key[:key_index] + key_letter + key[key_index + 1:]

    return decrypt_with_key(key, encrypted_text), key
# end: def solve


# ====================================================================================================
# def main
#
# The main function to handle the solving routine
#
# Arguments--
#
# encrypted_text:	the text to solve for
#
def main(encrypted_text: str):
    print("INFO -- Will clean up encrypted_text...")
    encrypted_text = clean_cipher_text(encrypted_text)
    print("\tDone.")
    print("INFO -- Will begin solving...")
    ans, key = solve(encrypted_text)
    print("\tDone.")
    return ans, key
# end: def main


# ====================================================================================================
# def run_test
#
# Run the cipher solve program with an expected answer to check accuracy
#
# Arguments--
#
# test_name:		the name of the test to print out for clarity
#
# encrypted_text:	the encrypted version of expected; what the program should try to decrypt
#
# expected:			the expected decrypted string
#
def run_test(test_name, encrypted_text, expected):
    print("--------------------------------------------------")
    print(f"INFO -- Test {test_name}")
    ans, key = main(encrypted_text)
    
    # Source: https://stackoverflow.com/questions/17388213/find-the-similarity-metric-between-two-strings
    w1 = ans + ' ' * (len(expected) - len(ans))
    w2 = expected + ' ' * (len(ans) - len(expected))
    accuracy: int = sum(1 if i == j else 0 for i, j in zip(w1, w2)) / float(len(w1)) * 100

    print(f"ANS: {ans}\n\t" +
          f"KEY: {key}\n\t" + 
          f"% CORRECT: {accuracy}\n")
# end: def run_test


# call to main
if __name__ == "__main__":
    print("INFO -- Will init words_by_patterns...")
    init_word_patterns()
    print("\tDone.")

    # If the user just ran the python file, then demonstrate the capabilities of the program by running tests
    # on some common mono-alphabetic ciphers. Also inform the user that they can run their own text
    if (len(sys.argv) <= 1):
        print("INFO -- No text specified, will run with example text\n\t" +
              f"Use python3 mono_substitution_solver.py <text...> to load custom encrypted text\n\t" +
              f"Make sure to surround strings with quotes")

        expected = "if he had anything confidential to say he wrote it in cipher that is by so changing the order of the letters of the alphabet that not a word could be made out because sometimes we all have information that we might want to hide in an encoded form especially if we were to be part of a war or conflict where access to information could change the course of the fight for us it is important to hide the information from people who might want to uncover it"
        # Source for encoding: https://cryptii.com/pipes/caesar-cipher (shift = 7)
        run_test("1: CAESAR", "pm ol ohk hufaopun jvumpkluaphs av zhf ol dyval pa pu jpwoly aoha pz if zv johunpun aol vykly vm aol slaalyz vm aol hswohila aoha uva h dvyk jvbsk il thkl vba iljhbzl zvtlaptlz dl hss ohcl pumvythapvu aoha dl tpnoa dhua av opkl pu hu lujvklk mvyt lzwljphssf pm dl dlyl av il whya vm h dhy vy jvumspja dolyl hjjlzz av pumvythapvu jvbsk johunl aol jvbyzl vm aol mpnoa mvy bz pa pz ptwvyahua av opkl aol pumvythapvu myvt wlvwsl dov tpnoa dhua av bujvcly pa", expected)
        # Source for encoding: http://rumkin.com/tools/cipher/atbash.php
        run_test("2: ATBASH", "ru sv szw zmbgsrmt xlmurwvmgrzo gl hzb sv dilgv rg rm xrksvi gszg rh yb hl xszmtrmt gsv liwvi lu gsv ovggvih lu gsv zokszyvg gszg mlg z dliw xlfow yv nzwv lfg yvxzfhv hlnvgrnvh dv zoo szev rmulinzgrlm gszg dv nrtsg dzmg gl srwv rm zm vmxlwvw ulin vhkvxrzoob ru dv dviv gl yv kzig lu z dzi li xlmuorxg dsviv zxxvhh gl rmulinzgrlm xlfow xszmtv gsv xlfihv lu gsv urtsg uli fh rg rh rnkligzmg gl srwv gsv rmulinzgrlm uiln kvlkov dsl nrtsg dzmg gl fmxlevi rg", expected)
        # Source for encoding: https://cryptii.com/pipes/caesar-cipher
        run_test("3: ROT 13", "vs ur unq nalguvat pbasvqragvny gb fnl ur jebgr vg va pvcure gung vf ol fb punatvat gur beqre bs gur yrggref bs gur nycunorg gung abg n jbeq pbhyq or znqr bhg orpnhfr fbzrgvzrf jr nyy unir vasbezngvba gung jr zvtug jnag gb uvqr va na rapbqrq sbez rfcrpvnyyl vs jr jrer gb or cneg bs n jne be pbasyvpg jurer npprff gb vasbezngvba pbhyq punatr gur pbhefr bs gur svtug sbe hf vg vf vzcbegnag gb uvqr gur vasbezngvba sebz crbcyr jub zvtug jnag gb hapbire vg", expected)
        # Source for encoding: https://cryptii.com/pipes/caesar-cipher (slope = 5, int = 8)
        run_test("4: AFFINE", "wh rc rix ivyzrwvm savhwxcvzwil za uiy rc opazc wz wv swfrcp zriz wu ny ua srivmwvm zrc apxcp ah zrc lczzcpu ah zrc ilfrincz zriz vaz i oapx saelx nc qixc aez ncsieuc uaqczwqcu oc ill rijc wvhapqizwav zriz oc qwmrz oivz za rwxc wv iv cvsaxcx hapq cufcswilly wh oc ocpc za nc fipz ah i oip ap savhlwsz orcpc isscuu za wvhapqizwav saelx srivmc zrc saepuc ah zrc hwmrz hap eu wz wu wqfapzivz za rwxc zrc wvhapqizwav hpaq fcaflc ora qwmrz oivz za evsajcp wz", expected)


    # If the user did specify other arguments to the command line when running the program, assume they are
    # encrypted text(s) to decrypt
    else:
        # Useful for test cases: http://www.dummytextgenerator.com/#jump
        # When generating filler text, just make sure to select "Use English words"

        # Loop through each of the arguments passed in and run it through the program. If the text is short, the
        # program may not be able to decode it very well or at all so warn the user about that
        for i in range(1, len(sys.argv)):
            encrypted_text: str = sys.argv[i]
            if (len(encrypted_text.split()) <= 100):
                print(f"WARN -- encrypted text {i} contains {len(encrypted_text.split())} words! " +
                      "Decryption may not be possible (>100 words is recommended to ensure a readable ~70% correct)")
                continue_input = ""
                while (continue_input.lower() != "y" and continue_input.lower() != "n"):
                    continue_input = input("\tContinue decryption anyway? (y/n): ")
                if (continue_input.lower() == "n"):
                    continue
            
            ans, key = main(encrypted_text)
            print(f"ANS: {ans}\n\t" +
                  f"KEY: {key}")
# end: call to main
