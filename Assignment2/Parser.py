class Parser:
    def __init__(self, obj):
        self.symbols = obj.tokens
    def parse(self):
        for i in self.symbols:
            print(i.lexeme, i.tCode)