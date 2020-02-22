# Simple Password Generator

import string as s
from random import randrange


char = f"[/*-+!@#$%^&*()+:;?,.<>]"
num1 = "0123456789"
small = s.ascii_lowercase
caps = s.ascii_uppercase
Apasswd = char + num1 + small + caps
passwd = num1 + small





class Gen_Pass_Adv:

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
            self.password += Apasswd[pick]

        print(self.password)



class Gen_Pass:

    def __init__(self, number, _vchar):
        self.char_length = len(_vchar)
        self.default = 10
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

    print("Choose Password Strength")
    print("Strong : Enter 1")
    print("Weak : Enter 2")
    ch = int(input())

    print("Enter Length of Password Required")
    num = input("")

    if ch == 1:
        Gen_Pass_Adv(num, Apasswd)
    else:
        Gen_Pass(num, passwd)




