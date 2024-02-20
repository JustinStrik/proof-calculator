from scanner import *
from mathparser import *
from token_ import *
from AST import *

# make ast of the input string using ast module
inputstring = '23 * (3 + 4)'
parser = Parser(inputstring)
ast = parser.parse()


