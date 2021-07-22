import pytest

from main import Caesar
from main import Alphabet


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("b arf", "o nes"),
        ("b.arf", "o.nes"),
        ("aaa*a**", "nnn*n**"),
        ("aaa.)", "nnn.)"),
        (".....//////nnnnn***", ".....//////aaaaa***"),


    ],
)
def test_cipher_eng(test_input, expected_output):
    lat_alphabet = Alphabet([chr(x) for x in range(ord("a"), ord("z") + 1)])
    c = Caesar(lat_alphabet)
    crypt_result = c.crypt(test_input)
    encrypt_result = c.encrypt(expected_output)
    assert crypt_result == expected_output
    assert encrypt_result == test_input


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
       ("енот", "тъыя"),
       ("месяц", "щтюмг"),
       ("заяц", "фнмг"),
       ("жизнь", "ухфъй"),
       ("оывсивтбю", "ыипюхпяол")

    ],
)
def test_cipher_rus(test_input, expected_output):
    kir_alphabet = Alphabet([chr(x) for x in range(ord("а"), ord("я") + 1)])
    c = Caesar(kir_alphabet)
    crypt_result = c.crypt(test_input)
    encrypt_result = c.encrypt(expected_output)
    assert crypt_result == expected_output
    assert encrypt_result == test_input



