import pytest

from main import Caesar
from main import Message
from main import Operation


@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("b arf", "o nes"),
        ("b.arf", "o.nes"),
        ("aaa*a**", "nnn*n**"),
        ("aaa.)", "nnn.)"),
        (".....//////nnnnn***", ".....//////aaaaa***"),
        ("енот", "тъыя"),
       ("месяц", "щтюмг"),
       ("заяц", "фнмг"),
       ("жизнь", "ухфъй"),
       ("оывсивтбю", "ыипюхпяол")


    ],
)
def test_crypt(test_input, expected_output):
    msg = Message(test_input)
    operation = Operation("CRYPT")
    c = Caesar(msg)
    result = c.text_handling(operation)
    assert result == expected_output




@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("b arf", "o nes"),
        ("b.arf", "o.nes"),
        ("aaa*a**", "nnn*n**"),
        ("aaa.)", "nnn.)"),
        (".....//////nnnnn***", ".....//////aaaaa***"),
        ("енот", "тъыя"),
       ("месяц", "щтюмг"),
       ("заяц", "фнмг"),
       ("жизнь", "ухфъй"),
       ("оывсивтбю", "ыипюхпяол")

    ],
)
def test_encrypt(test_input, expected_output):
    msg = Message(expected_output)
    operation = Operation("ENCRYPT")
    c = Caesar(msg)
    result = c.text_handling(operation)
    assert result == test_input









