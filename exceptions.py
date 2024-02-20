# make all exceptions types and messages

# Lexical, Syntax, TypeCheck
# write a function to raise exceptions and when to raise them

class LexicalException(Exception):
    def __init__(self, message):
        self.message = message

class SyntaxException(Exception):
    def __init__(self, message):
        self.message = message

class TypeCheckException(Exception):
    def __init__(self, message):
        self.message = message

