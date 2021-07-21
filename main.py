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
    f = True
    while f:
        print("Enter the text:")
        text = input()
        print("If you desire to crypt text then print CRYPT else ENCRYPT")
        ans = input()
        if ans == "CRYPT":
            print(c.crypt(text))
        elif ans == "ENCRYPT":
            print(c.encrypt(text))
        else:
            print("wrong answer")
        print("Do you want continue? print YES ")
        f = input() == "YES"

if __name__ == "__main__":
    c = Caesar()

    print ("Do you want to use user input? YES or NO")
    ans = input()
    if ans == "YES":
        user_input()
    elif ans == "NO":
        print("Some tests for example: ")
        print(c.crypt("b arf"))
        print(c.crypt("aa.a"))
        print(c.crypt("aaa.)"))
        print(c.crypt(".....//////nnnnn***"))
    else:
        print("Wrong answer")
