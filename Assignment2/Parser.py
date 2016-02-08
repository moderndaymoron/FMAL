from Token import Token


import sys
TokenCode = { 'ID':1, 'ASSIGN':2, 'SEMICOL':3, 'INT':4, 'ADD':5,
 'SUB':6, 'MULT':7, 'LPAREN':8, 'RPAREN':9, 'PRINT':10, 'END':11, 'ERROR':12}

class Parser:

    stack = []

    def __init__(self, obj):
        self.lexer = obj
        self.token = self.lexer.nextToken()
        self.oldtoken = self.token

    def parse(self):
            self.statements()
            self.printOutput()

    def statements(self):
        if self.token is None or self.token.tCode == TokenCode['END']:
            return
        self.statement()
        self.statements()

    def statement(self):
        if self.accept(TokenCode['SEMICOL']):
            return
        elif self.accept(TokenCode['ID']):
            self.stack.append('PUSH ' + self.oldtoken.lexeme)
            if self.accept(TokenCode['ASSIGN']):
                self.expr()
                self.stack.append('ASSIGN')
            else:
                self.error()
        elif self.accept(TokenCode['PRINT']):
            if self.accept(TokenCode['ID']):
                self.stack.append('PUSH ' + self.oldtoken.lexeme)
                self.stack.append('PRINT')
                return
            else:
                self.error()
        else:
            self.error()

    def expr(self):
        self.term()
        if self.accept(TokenCode['ADD']):
            self.expr()
            self.stack.append('ADD')
        elif self.accept(TokenCode['SUB']):
            self.expr()
            self.stack.append('SUB')

    def term(self):
        self.factor()
        if self.accept(TokenCode['MULT']):
            self.term()
            self.stack.append('MULT')

    def factor(self):
        if self.accept(TokenCode['INT']) or self.accept(TokenCode['ID']):
            self.stack.append('PUSH ' + self.oldtoken.lexeme)
        elif self.accept(TokenCode['LPAREN']):
            self.expr()
            if self.accept(TokenCode['RPAREN']):
                return
            else:
                self.error()
        else:
            self.error()

    def error(self):
        self.stack.append('ERROR')

    def accept(self, symbol):
        if symbol == self.token.tCode:
            if not self.token.tCode == TokenCode['END']:
                self.oldtoken = self.token
                self.token = self.lexer.nextToken()
            return True
        return False

    def printOutput(self):
        for i in self.stack:
            if i == 'ERROR':
                print("Syntax error!")
                return
            sys.stdout.write(i + '\n')
