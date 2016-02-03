from enum import Enum
import sys
from Token import Token
TokenCode = Enum('TokenCode', 'ID ASSIGN SEMICOL INT ADD SUB MULT LPAREN RPAREN PRINT END ERROR')


class Lexer:
    tokens = []

    def __init__(self):
        inp = self.readInput()
        self.getPatterns(inp)

    def readInput(self):
        inp = input()
        return inp

    def nextToken(self, inp):
        if inp[0] == "=":
            token = Token(inp[0], 2)
            self.tokens.append(token)
        elif inp[0] == ";":
            token = Token(inp[0], 3)
            self.tokens.append(token)
        elif inp[0] == "+":
            token = Token(inp[0], 5)
            self.tokens.append(token)
        elif inp[0] == "-":
            token = Token(inp[0], 6)
            self.tokens.append(token)
        elif inp[0] == "*":
            token = Token(inp[0], 7)
            self.token.append(token)
        elif inp[0] == "(":
            token = Token(inp[0], 8)
            self.token.append(token)
        elif inp[0] == ")":
            token = Token(inp[0], 9)
            self.token.append(token)
        elif inp[0].isdigit():
            inp = self.checkDigit(inp)
            return inp
        elif inp[0].isalpha():
            inp = self.checkIdentifier(inp)
            return inp
        else:
            token = Token(inp[0], 12)

        return inp[1:]

    def getPatterns(self, inp):
        if not inp:
            return

        inp = self.nextToken(inp)
        return self.getPatterns(inp)

    def checkDigit(self, inp):
        digit = ""
        while inp[0].isdigit():
            digit += inp[0]
            inp = inp[1:]

            if not inp:
                break

        token = Token(digit, 4)
        self.tokens.append(token)
        return inp

    def checkIdentifier(inp):
        identifier = ""
        if inp[:3] == "end" and len(inp) > 3 and not inp[4].isalpha():
            self.token.append(inp[:3], 11)
        elif inp[:5] == "print" and not inp[6].isalpha():
        while inp[0].isalpha():
