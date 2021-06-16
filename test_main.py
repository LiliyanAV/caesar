import pytest

from main import Caesar


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
def test_crypt_py(test_input, expected_output):
    c = Caesar()
    result = c.crypt(test_input)
    assert result == expected_output
