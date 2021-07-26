languages = {
    'en': 'rus'
}

alphabets = {
    'en': [chr(x) for x in range(ord("a"), ord("z") + 1)],
    'rus': [chr(x) for x in range(ord("а"), ord("я") + 1)]
}


class Alphabet:
    def __init__(self, key):
        if key in alphabets.keys():
            self.symbols = alphabets[key]
        else:
            print("Could not recognize alphabet")

    def __len__(self):
        return len(self.symbols)

    def chr_in(self, ch):
        return ch in self.symbols

    def text_accessory(self, text):
        for ch in text:
            if self.chr_in(ch):
                return True
        return False


def text_classification(text):
    for key in alphabets.keys():
        a = Alphabet(key)
        if a.text_accessory(text):
            return a


class Message:
    def __init__(self, text):
        self.alphabet = text_classification(text)
        self.text = text


Operations = {"CRYPT",
              "ENCRYPT"}


class Operation:
    def __init__(self, operation):
        if operation in Operations:
            self.value = operation
        else:
            print("Wrong kind of operation, CRYPT will be use as default")
            self.value = "CRYPT"


def mistake_handl(sh):
    error = "Wrong value as default will be use 13"
    try:
        shift = int(sh)
    except ValueError:
        print(error)
        shift = 13
    else:
        if shift <= 0:
            print(error)
            shift = 13

    return shift


class Shift:
    def __init__(self, sh):
        self.value = mistake_handl(sh)


class Caesar:
    def __init__(self, msg, shift = Shift(13)):
        self.shift = shift.value
        self.msg = msg

    def chr_shift(self, shift, ch):
        if ch in self.msg.alphabet.symbols:
            return chr((ord(ch) - ord(self.msg.alphabet.symbols[0]) + shift) % len(self.msg.alphabet)
                       + ord(self.msg.alphabet.symbols[0]))
        return ch

    def answer_gen(self, shift):
        return "".join([self.chr_shift(shift, ch) for ch in self.msg.text])

    def text_handling(self, operation):
        if operation.value == "CRYPT":
            return self.answer_gen(self.shift)
        return self.answer_gen(-self.shift)


def user_input():
    while input():
        msg = Message(input("Enter the text: "))
        shift = Shift(input("Enter the shift: "))
        operation = Operation(input("If you desire to crypt text then print CRYPT else ENCRYPT "))
        c = Caesar(msg, shift)
        print(c.text_handling(operation))


if __name__ == "__main__":
    words = ["th.e", "q.u..ick", "bro7wn", "fo-x", "ju*m*ps", "o-v#er", "t++he", "l;azy", "d$og", "b arf", "aa.a",
             "aaa.)", ".....//////nnnnn***"]

    ans = input("Do you want to use user input? YES or NO ")
    if ans == "YES":
        user_input()
    elif ans == "NO":
        print("Some tests for example: ")
        for word in words:
            msg = Message(word)
            op_crypt = Operation("CRYPT")
            op_encrypt = Operation("ENCRYPT")
            c = Caesar(msg)

            print("Initial word: " + word + "; Crypted word: " +
                  c.text_handling(op_crypt) + "; Encrypted word:" + c.text_handling(op_encrypt))
    else:
         print("Wrong answer")
