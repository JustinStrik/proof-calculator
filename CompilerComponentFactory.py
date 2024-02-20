from scanner import Scanner
from mathparser import Parser
from token_ import Token
from AST import AST

class CompilerComponentFactory:
    def makeScanner(inputstring):
        return Scanner(inputstring)
                       
    def makeMathParser(inputstring):
        return Parser(inputstring)
    
    def makeTypeChecker():
        return TypeChecker()