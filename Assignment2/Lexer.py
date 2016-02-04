import sys
from Token import Token

class Lexer:

    def __init__(self):
        self.inp = self.readinput()

    def readinput(self):
        inp = input()
        return inp

    def nextToken(self):
        if not self.inp:
            return False
        if self.inp[0] == "=":
            token = Token(self.inp[0], 2)
        elif self.inp[0] == ";":
            token = Token(self.inp[0], 3)
        elif self.inp[0] == "+":
            token = Token(self.inp[0], 5)
        elif self.inp[0] == "-":
            token = Token(self.inp[0], 6)
        elif self.inp[0] == "*":
            token = Token(self.inp[0], 7)
        elif self.inp[0] == "(":
            token = Token(self.inp[0], 8)
        elif self.inp[0] == ")":
            token = Token(self.inp[0], 9)
        elif self.inp[0].isdigit():
            token = self.checkDigit()
            return token
        elif self.inp[0].isalpha():
            token = self.checkIdentifier()
            return token
        else:
            token = Token(self.inp[0], 12)

        self.inp = self.inp[1:]
        return token

    def checkDigit(self):
        digit = ""
        while self.inp[0].isdigit():
            digit += self.inp[0]
            self.inp = self.inp[1:]

            if not self.inp:
                break

        return Token(digit, 4)

    def checkIdentifier(self):
        identifier = ""
        if self.inp[:3] == "end":
            if len(self.inp) >= 4:
                if not self.inp[3].isalpha():
                    symbol = self.inp[:3]
                    self.inp = self.inp[3:]
                    return Token(symbol, 11)
            else:
                symbol = self.inp[:3]
                self.inp = self.inp[3:]
                return Token(symbol, 11)

        elif self.inp[:5] == "print":
            if len(self.inp) >= 6:
                if not self.inp[5].isalpha():
                    symbol = self.inp[:5]
                    self.inp = self.inp[5:]
                    return Token(symbol, 10)

        while self.inp[0].isalpha() or self.inp[0].isdigit():
            identifier += self.inp[0]
            self.inp = self.inp[1:]

            if not self.inp:
                break

        return Token(identifier, 1)

    def printTokens(self):
        for i in self.tokens:
            
            print(i.lexeme, i.tCode)
