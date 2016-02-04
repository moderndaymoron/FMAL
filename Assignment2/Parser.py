from Token import Token
from enum import Enum
TokenCode = Enum('TokenCode', 'ID ASSIGN SEMICOL INT ADD SUB MULT LPAREN RPAREN PRINT END ERROR')


class Parser:
    token = Token(None, None)

    def __init__(self, obj):
        self.lexer = obj

    def parse(self):
        while True:
            token = self.lexer.nextToken()
            if not token:
                break
            print(token.lexeme, token.tCode)
            #main logic replaces this
            #self.symbols.nextToken should be used heavily here

    def statements(self, c):
        pass

    def statements(self, c):
        pass

    def expr(self, c):
        pass

    def term(self, c):
        pass

    def factor(self, c):
        pass
