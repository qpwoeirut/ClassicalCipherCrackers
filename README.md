# ClassicalCipherCracker
A (hopefully) considerably copious collection of crackers for classical ciphers

Written in Python3 (and run with PyPy)

## TODOs
* Write a "text fitness evaluator" function which evaluates the likelihood that a given string of text is English
* Write a substitution cipher decoder (which can also server as a ROT13, Caesar, and Atbash decoder)
* Investigate using AI to identify what cipher a ciphertext might be encrypted with
* Compile a list of common classical ciphers (drawing from Wikipedia and the National Cipher Competition)


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
