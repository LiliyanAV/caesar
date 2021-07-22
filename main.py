class Alphabet:
    def __init__(self, symbols):
        self.symbols = symbols
        self.size = len(self.symbols)

    def chr_inside(self, ch):
        return ch in self.symbols

    def mess_classification(self, message):
        f = False
        for ch in message:
            f = self.chr_inside(ch)
            if f:
                break
        return f


class Caesar:
    def __init__(self, alphabet, shift=13):
        self.shift = shift
        self.alphabet = alphabet

    def crypt_chr(self, ch):
        if ch not in self.alphabet.symbols:
            return ch
        return chr((ord(ch) - ord(self.alphabet.symbols[0]) + self.shift) % self.alphabet.size
                   + ord(self.alphabet.symbols[0]))

    def crypt(self, text):
        text.lower()
        return "".join([self.crypt_chr(ch) for ch in text])

    def encrypt_chr(self, ch):
        if ch not in self.alphabet.symbols:
            return ch
        return chr((ord(ch) - ord(self.alphabet.symbols[0]) - self.shift) % self.alphabet.size
                   + ord(self.alphabet.symbols[0]))

    def encrypt(self, encoded_text):
        encoded_text.lower()
        return "".join([self.encrypt_chr(ch) for ch in encoded_text])


def user_input():
    while input():
        text = input("Enter the text: ")
        shift = int(input("Enter the shift: "))
        if kir_alphabet.mess_classification(text):
            c = Caesar(kir_alphabet, shift)
        else:
            c = Caesar(lat_alphabet, shift)
        ans = input("If you desire to crypt text then print CRYPT else ENCRYPT ")
        if ans == "CRYPT":
            print(c.crypt(text))
        elif ans == "ENCRYPT":
            print(c.encrypt(text))
        else:
            print("Wrong answer")


if __name__ == "__main__":

    lat_alphabet = Alphabet([chr(x) for x in range(ord("a"), ord("z") + 1)])
    kir_alphabet = Alphabet([chr(x) for x in range(ord("а"), ord("я") + 1)])

    ru = Caesar(kir_alphabet)

    c_ex = Caesar(lat_alphabet)
    words = ["th.e", "q.u..ick", "bro7wn", "fo-x", "ju*m*ps", "o-v#er", "t++he", "l;azy", "d$og", "b arf", "aa.a",
             "aaa.)", ".....//////nnnnn***"]

    ans = input("Do you want to use user input? YES or NO ")
    if ans == "YES":
        user_input()
    elif ans == "NO":
        print("Some tests for example: ")
        for word in words:
            print("Initial word: " + word + "; Crypted word: "
                  + c_ex.crypt(word) + "; Encrypted word:" + c_ex.encrypt(word))
    else:
        print("Wrong answer")
