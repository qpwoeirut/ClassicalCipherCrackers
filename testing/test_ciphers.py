from ciphers.AffineCipher import AffineCipher
from ciphers.AutokeyCipher import AutokeyCipher
from ciphers.CaesarCipher import CaesarCipher
from ciphers.Cipher import Cipher
from ciphers.ColumnarTranspositionCipher import ColumnarTranspositionCipher
from ciphers.HillCipher import HillCipher
from ciphers.MonoSubstitutionCipher import MonoSubstitutionCipher
from ciphers.MyszkowskiTranspositionCipher import MyszkowskiTranspositionCipher
from ciphers.PlayfairCipher import PlayfairCipher
from ciphers.RailFenceCipher import RailFenceCipher
from ciphers.VigenereCipher import VigenereCipher
from util import ALPHABET_IJ_MERGED


def test_cipher(cipher: Cipher, plaintext: str, ciphertext: str):
    assert cipher.encrypt(plaintext) == ciphertext, cipher.encrypt(plaintext)
    assert cipher.decrypt(ciphertext) == plaintext, cipher.decrypt(ciphertext)


def run_tests():
    test_cipher(AffineCipher((5, 8)), "AFFINECIPHER", "IHHWVCSWFRCP")

    test_cipher(AutokeyCipher("QUEENLY"), "ATTACKATDAWN", "QNXEPVYTWTWP")

    # TODO add test for Beaufort cipher

    test_cipher(CaesarCipher(23),
                "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD")

    columnar_transposition_cipher = ColumnarTranspositionCipher((5, 2, 1, 3, 0, 4))
    test_cipher(columnar_transposition_cipher, "WEAREDISCOVEREDFLEEATONCEQKJEU", "EVLNEACDTKESEAQROFOJDEECUWIREE")
    test_cipher(columnar_transposition_cipher, "WEAREDISCOVEREDFLEEATONCE", "EVLNACDTESEAROFODEECWIREE")

    test_cipher(MyszkowskiTranspositionCipher("TOMATO"), "WEAREDISCOVEREDFLEEATONCE", "ROFOACDTEDSEEEACWEIVRLENE")

    test_cipher(HillCipher("GYBNQKURP"), "ACTCAT", "POHFIN")

    monoalphabetic_substitution_cipher = MonoSubstitutionCipher("ZEBRASCDFGHIJKLMNOPQTUVWXY")
    test_cipher(monoalphabetic_substitution_cipher, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ZEBRASCDFGHIJKLMNOPQTUVWXY")
    test_cipher(monoalphabetic_substitution_cipher,
                "flee at once. we are discovered!".upper(), "SIAA ZQ LKBA. VA ZOA RFPBLUAOAR!")

    test_cipher(PlayfairCipher("PLAYFIREXMBCDGHKNOQSTUVWZ", alphabet=ALPHABET_IJ_MERGED),
                "HIDETHEGOLDINTHETREXESTUMP", "BMODZBXDNABEKUDMUIXMMOUVIF")

    test_cipher(RailFenceCipher((4, 3)), "abcdefghijklmnop", "djpceikobfhlnagm")
    test_cipher(RailFenceCipher((3, 0)), "WEAREDISCOVEREDRUNATONCE", "WECRUOERDSOEERNTNEAIVDAC")

    test_cipher(VigenereCipher("LEMON"), "ATTACKATDAWN", "LXFOPVEFRNHR")


if __name__ == '__main__':
    run_tests()
