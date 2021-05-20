class Caesar:
    def __init__(self):
        self.shift = 13
        self.alpha = [chr(x) for x in range(ord('a'), ord('z') + 1)]
        self.size = ord('z') - ord('a') + 1

    def crypt_chr(self, ch):
       return chr((ord(ch) - ord('a') + self.shift) % self.size + ord('a')) if ch in self.alpha else ch

    def crypt(self, text):
        text.lower()
        return "".join([self.crypt_chr(ch) for ch in text])

    def encrypt(self, encoded_text):
        return self.crypt(self, encoded_text)


if __name__ == '__main__':
    c = Caesar()
    print(c.crypt("b arf"))
    print(c.crypt("aaaa"))
