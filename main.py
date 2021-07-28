from enum import Enum

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

    def __contains__(self, item):
        return item in self.symbols

    def __index__(self):
        return self.symbols[0]


def text_alphabet(alphabet, text):
    for ch in text:
        if alphabet.__contains__(ch):
            return True
        return False


def text_classification(text):
    for key in alphabets.keys():
        alphabet = Alphabet(key)
        if text_alphabet(alphabet, text):
            return alphabet


class Message:
    def __init__(self, text):
        self.alphabet = text_classification(text)
        self.text = text


class Operation(Enum):
    CRYPT = "CRYPT"
    ENCRYPT = "ENCRYPT"


def create_operation(str):
    try:
        op = Operation[str]

    except KeyError:
        print("Wrong kind of operation. CRYPT will be use")
        op = Operation["CRYPT"]
    return op


class Shift:
    def __init__(self):
        self.value = 13

    @property
    def set_value(self):
        return self.value

    @set_value.setter
    def set_value(self, val):
        error = "Wrong value as default will be use 13"
        try:
            self.value = int(val)
            if self.value <= 0:
                raise ValueError
        except ValueError:
            print(error)


class Caesar:
    def __init__(self, msg, shift=Shift()):
        self.shift = shift.value
        self.msg = msg

    def chr_shift(self, shift, ch):
        if ch in self.msg.alphabet.symbols:
            return chr((ord(ch) - ord(self.msg.alphabet.symbols[0]) + shift) % len(self.msg.alphabet)
                       + ord(self.msg.alphabet[0]))
        return ch

    def text_shift(self, shift):
        return "".join([self.chr_shift(shift, ch) for ch in self.msg.text])

    def text_handling(self, operation):
        if operation == Operation.CRYPT:
            return self.text_shift(self.shift)
        return self.text_shift(-self.shift)


def user_input():
    while input():
        msg = Message(input("Enter the text: "))
        shift = Shift()
        shift.value = input("Enter the shift: ")
        operation = create_operation(input("If you desire to crypt text then print CRYPT else ENCRYPT "))
        c = Caesar(msg, shift)
        print(c.text_handling(operation))


if __name__ == "__main__":
    words = ["th.e", "q.u..ick", "bro7wn", "fo-x", "ju*m*ps", "o-v#er", "t++he", "l;azy", "d$og", "b arf", "aa.a",
             "aaa.)", ".mm....nmnmnmn***"]

    ans = input("Do you want to use user input? YES or NO ")
    if ans == "YES":
        user_input()
    elif ans == "NO":
        print("Some tests for example: ")
        for word in words:
            msg = Message(word)
            op_crypt = create_operation("CRYPT")
            op_encrypt = create_operation("ENCRYPT")
            c = Caesar(msg)

            print("Initial word: " + word + "; Crypted word: " +
                  c.text_handling(op_crypt) + "; Encrypted word:" + c.text_handling(op_encrypt))
    else:
        print("Wrong answer")
