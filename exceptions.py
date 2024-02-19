# make all exceptions types and messages

# Lexical, Syntax, TypeCheck
# write a function to raise exceptions and when to raise them

class LexicalError(Exception):
    def __init__(self, message):
        self.message = message

class SyntaxError(Exception):
    def __init__(self, message):
        self.message = message

class TypeCheckError(Exception):
    def __init__(self, message):
        self.message = message

