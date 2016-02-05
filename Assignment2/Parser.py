from Token import Token
import sys
TokenCode = { 'ID':1, 'ASSIGN':2, 'SEMICOL':3, 'INT':4, 'ADD':5,
 'SUB':6, 'MULT':7, 'LPAREN':8, 'RPAREN':9, 'PRINT':10, 'END':11, 'ERROR':12}

class Parser:
    commands = []
    S = []

    def __init__(self, obj):
        self.lexer = obj
        self.token = self.lexer.nextToken()

    def parse(self):
            self.statements()
            self.printOutput()
            #main logic replaces this
            #self.symbols.nextToken should be used heavily here

    def statement(self):
        if self.accept(TokenCode['ID']):
            self.S.append('PUSH ' + self.token.lexeme)
            self.token = self.lexer.nextToken()
            if self.accept(TokenCode['ASSIGN']):
                self.commands.append('ASSIGN')
                self.token = self.lexer.nextToken()
                self.expr();
            else: 
                self.error("statement if ASSIGN")
        elif self.accept(TokenCode['PRINT']):
            self.commands.append('PRINT')
            self.token = self.lexer.nextToken()
            if self.accept(TokenCode['ID']) or self.accept(TokenCode['INT']):
                self.S.append('PUSH ' + self.token.lexeme)
                self.token = self.lexer.nextToken()
            else: self.error("statement second from bot")
        else:
            print(self.token.lexeme) 
            self.error("statement bot")

    def statements(self):
            self.statement() 
            if self.accept(TokenCode['SEMICOL']):
                self.moveStack()
            self.token = self.lexer.nextToken()
            if self.accept(TokenCode['END']):
                return
            self.statements()

    def expr(self):
        self.term()
        if self.accept(TokenCode['ADD']) or self.accept(TokenCode['SUB']):
            if self.accept(TokenCode['ADD']):
                self.commands.append('ADD')
            else: self.commands.append('SUB')
            self.token = self.lexer.nextToken()
            self.term()
            self.moveOne()

    def term(self):
        self.factor()
        while self.accept(TokenCode['MULT']):
            self.token = self.lexer.nextToken()
            self.commands.append('MULT')
            self.factor()

    def factor(self):
        if self.accept(TokenCode['ID']) or self.accept(TokenCode['INT']):
            self.S.append('PUSH ' + self.token.lexeme)
            self.token = self.lexer.nextToken()
        elif self.accept(TokenCode['LPAREN']):
            self.token = self.lexer.nextToken()
            self.expr()
            if self.accept(TokenCode['RPAREN']):
                self.token = self.lexer.nextToken()
        else: self.error("factor")

    def accept(self, symbol):
        if symbol == self.token.tCode:
            return True
        return False
    
    def error(self, msg):
        print(msg)
        self.commands.append('ERROR')

    def expect(self, symbol):
        if symbol == self.token.tCode:
            return True
        self.error()

    def moveStack(self):
        for i in range(len(self.commands)):
            self.S.append(self.commands.pop())

    def moveOne(self):
        self.S.append(self.commands.pop())

    def printOutput(self):
        for i in self.S:
            if i == 'ERROR':
                print("Syntax error!")
                return
            sys.stdout.write(i + '\n')