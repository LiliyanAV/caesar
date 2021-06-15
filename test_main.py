from main import Caesar


def test_crypt():
    c = Caesar()
    assert c.crypt("b arf") == "o nes"
    assert c.crypt("b.arf") == "o.nes"
    assert c.crypt("aaa*a**") == "nnn*n**"
    assert c.crypt("aaa.)") == "nnn.)"
    assert c.crypt(".....//////nnnnn***") == ".....//////aaaaa***"
