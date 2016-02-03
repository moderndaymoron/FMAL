from enum import Enum
import sys
import Token
TokenCode = Enum('TokenCode', 'ID ASSIGN SEMICOL INT ADD SUB MULT LPAREN RPAREN PRINT END ERROR')
class Lexer:
    tokens = []
    def __inti__(self):
        pass
    def nextToken():
        while True:
    	    c = sys.stdin.read(1)
    	    if c == "=":
    	        token = Token("=", 2)
    		    tokens.append(token)
            elif c == ";":
    	        token = Token(";", 3)
    		    tokens.append(token)
            elif c == "+":
    		    pass
            elif c == "-":
                pass
            elif c == "*":
                pass
            elif c == "(":
                pass
            elif c == ")":
                pass
            elif c.isdigit():
                pass
            elif c.isalpha():
                pass
            else:
                pass
                #error