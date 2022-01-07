# ClassicalCipherCracker
A (hopefully) considerably copious collection of classical cipher crackers

Written in Python3 (and run with PyPy)

## TODOs
* Write a "text fitness evaluator" function which evaluates the likelihood that a given string of text is English
* Write a substitution cipher decoder (which can also server as a ROT13, Caesar, and Atbash decoder)
* Compile a list of common classical ciphers (drawing from Wikipedia and the National Cipher Competition)
* Write a word splitter which separates plaintext into words
* Investigate using AI to identify what cipher a ciphertext might be encrypted with
* Investigate using AI to evaluate text fitness


## Terminology
* __Plaintext__: a message which is readable and unencrypted
* __Ciphertext__: a message which is encrypted
* __Decoder__/__Decrypter__: a program which will decrypt a ciphertext _when given the key_
* __Cracker__: a program that can decrypt a ciphertext without the key, usually by making use of the decrypter


## Basic Methodology
A cracker has three major components: the key-finding algorithm, the decrypter, and the text evaluator.

The key-finding algorithm will generate keys which will be used by the decrypter to find the plaintext that the key would generate.
This plaintext will be tossed into the text evaluator.
If it gets a high score, the current key and plaintext will be saved as a possible answer.
As more keys get tested, the best key-plaintext pair will be continuously updated.

If the keyspace is small, then every key will be tested.
If brute force isn't feasible, a hill-climbing algorithm will be used, where random changes to the key are either kept or dropped if they create a better text evaluation.
The goal of the algorithm is to reach a "hill", where the plaintext is as likely to be the real message as possible.
Simulated annealing may also be used in the future.

Code should be written to prioritize speed when run under PyPy, though it should still be reasonably readable.
In particular, decrypters must be optimized to run quickly, as they are often called thousands of times in order to crack a cipher.
Different versions of decrypters should be tested and timed to determine which is most performant.
The same applies to the text fitness evaluator.


# Resources
## Text Fitness
http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/
<br>
https://medium.com/analytics-vidhya/how-to-distinguish-between-gibberish-and-valid-english-text-4975078c5688
<br>
https://planetcalc.com/7959/, https://planetcalc.com/8045/
<br>
https://gitlab.com/guballa/SubstitutionBreaker/-/blob/development/subbreaker/breaker.py

## Word Splitting
http://practicalcryptography.com/cryptanalysis/text-characterisation/word-statistics-fitness-measure/


