from Lexer import Lexer
from Parser import Parser
myLexer = Lexer()
myParser = Parser(myLexer)
myParser.parse()
