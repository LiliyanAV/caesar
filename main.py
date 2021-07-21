class Caesar:
    def __init__(self, shift=13):
        self.shift = shift
        self.alphabet = [chr(x) for x in range(ord("a"), ord("z") + 1)]
        self.size = len(self.alphabet)

    def crypt_chr(self, ch):
        if ch not in self.alphabet:
            return ch
        return chr((ord(ch) - ord("a") + self.shift) % self.size + ord("a"))

    def crypt(self, text):
        text.lower()
        return "".join([self.crypt_chr(ch) for ch in text])

    def encrypt(self, encoded_text):
        return self.crypt(encoded_text)


def user_input():

    while (input()):
        text = input("Enter the text: ")
        ans = input("If you desire to crypt text then print CRYPT else ENCRYPT ")
        if ans == "CRYPT":
            print(c.crypt(text))
        elif ans == "ENCRYPT":
            print(c.encrypt(text))
        else:
            print("Wrong answer")


if __name__ == "__main__":
    c = Caesar()
    words = ["th.e", "q.u..ick", "bro7wn", "fo-x", "ju*m*ps", "o-v#er", "t++he", "l;azy", "d$og", "b arf", "aa.a", "aaa.)",  ".....//////nnnnn***"]

    ans = input("Do you want to use user input? YES or NO ")
    if ans == "YES":
        user_input()
    elif ans == "NO":
        print("Some tests for example: ")
        for word in words:
            print("Initial word: " + word + "; Crypted word: "
                  + c.crypt(word) +"; Encrypted word:" + c.encrypt(word))
    else:
        print("Wrong answer")
