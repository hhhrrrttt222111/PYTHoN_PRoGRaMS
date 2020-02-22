# Simple Password Generator

import string as s
from random import randrange


char = f"[/*-+!@#$%^&*()+:;?,.<>]"
num1 = f"[1-9]"
small = s.ascii_lowercase
caps = s.ascii_uppercase
passwd = char + num1 + small + caps


class Gen_Pass:

    def __init__(self, number, _vchar):
        self.char_length = len(_vchar)
        self.default = 13
        self.num = number
        self.password = ""
        self.password_len = 0
        self.vchar = _vchar
        self.gen = self.generate()

    def generate(self):
        length = 0
        try:
            length = int(self.num)
        except ValueError:
            length = self.default


        while self.password_len is not length:
            pick = randrange(1,self.char_length)
            self.password_len += 1
            self.password += passwd[pick]

        print(self.password)


if "__main__" == __name__:
    print("Enter Length of Password Required")
    num = input("")
    Gen_Pass(num , passwd)

