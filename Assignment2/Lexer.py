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

    def checkIdentifier(self, inp):
        identifier = ""
        if inp[:3] == "end":
            if len(inp) >= 4:
                if not inp[3].isalpha():
                    self.tokens.append(inp[:3], 11)
                    return inp[3:]
            else:
                self.token.append(inp[:3], 11)
                inp = inp[3:]
                return inp

        elif inp[:5] == "print":
            if len(inp) >= 6:
                if not inp[5].isalpha():
                    self.tokens.append(inp[:5], 10)
                    return inp[5:]

        while inp[0].isalpha():
            identifier += inp[0]
            inp = inp[1:]

            if not inp:
                break

        token = Token(identifier, 1)
        self.tokens.append(token)
        return inp

    def printTokens(self):
        for i in self.tokens:
            
            print(i)
