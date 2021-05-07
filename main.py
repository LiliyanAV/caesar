class Caesar:
    def __init__(self):
        self.size = ord('z') - ord('a')+1
        self.shift = 13

    def crypt_chr(self, ch):
       return chr((ord(ch) - ord('a') + self.shift) % self.size + ord('a'))

    def crypt(self, text):
        text.lower()
        return "".join([self.crypt_chr(chr) for chr in text])

    def encrypt(self, encoded_text):
        return Caesar.crypt(self, encoded_text)

if __name__ == '__main__':
    c = Caesar()
    print(c.crypt("barf"))


