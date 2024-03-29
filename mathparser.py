# create a parser for math expressions that uses numpy
import numpy as np
import enum
import math
import re
import sys
import argparse
from node import *
from AST import AST
from scanner import Scanner

# define the grammar
# include exp, log, sin, cos, tan, sqrt, and pi, e, sum, mod, factorial, integral, derivative, parentheses, and the basic operations

# define priority of operations
# 1. parentheses
# 2. exponentiation
# 3. factorial
# 4. multiplication, division, modulo
# 5. addition, subtraction
# 6. sin, cos, tan, exp, log, sqrt, pi, e, sum, integral, derivative

# write a parser for the grammar

# write grammar
# Equation ::= Expression | = Expression
# PowExpr ::= AdditiveExpr ** PowExpr |   AdditiveExpr
# AdditiveExpr ::= MultiplicativeExpr ( ( + | - ) MultiplicativeExpr )*
# MultiplicativeExpr ::= Function (( * | / | % ) Function)*
# Function ::= - | sin(Expression) | cos(Expression) | tan(Expression) | exp(Expression) | log(Expression) | sqrt(Expression) | pi | e | sum(Expression) | mod(Expression) | integral(Expression) | derivative(Expression)
# PrimaryExpr ::= Number ( Expr ) | Z |
# x | y | a | r | inf
# Number ::= [0-9]+ | [0-9]+.[0-9]+ | [0-9]+. | .[0-9]+ | 0. | 0 | 0.0 | 0.0
# Parentheses ::= ( Expression )
# Operation ::= + | - | * | / | ^ | !
# Function ::= sin | cos | tan | exp | log | sqrt | pi | e | sum | mod | integral | derivative Parentheses
        

class TokenType(enum.Enum):
    T_NUM = 0
    T_PLUS = 1
    T_MINUS = 2
    T_MULT = 3
    T_DIV = 4
    T_LPAR = 5
    T_RPAR = 6
    T_EXP = 7
    T_FACT = 8
    T_SIN = 9
    T_COS = 10
    T_TAN = 11
    T_LOG = 12
    T_SQRT = 13
    T_PI = 14
    T_E = 15
    T_SUM = 16
    T_MOD = 17
    T_INTEGRAL = 18
    T_DERIVATIVE = 19
    T_END = 20

# class Token:
#     def __init__(self, type, value):
#         self.type = type
#         self.value = value

mappings = {
    '+': TokenType.T_PLUS,
    '-': TokenType.T_MINUS,
    '*': TokenType.T_MULT,
    '/': TokenType.T_DIV,
    '(': TokenType.T_LPAR,
    ')': TokenType.T_RPAR,
    '^': TokenType.T_EXP,
    '!': TokenType.T_FACT,
    'sin': TokenType.T_SIN,
    'cos': TokenType.T_COS,
    'tan': TokenType.T_TAN,
    'log': TokenType.T_LOG,
    'sqrt': TokenType.T_SQRT,
    'pi': TokenType.T_PI,
    'e': TokenType.T_E,
    'sum': TokenType.T_SUM,
    'mod': TokenType.T_MOD,
    'integral': TokenType.T_INTEGRAL,
    'derivative': TokenType.T_DERIVATIVE
}

# def lexical_analysis(s):
#     tokens = []

#     # change to work for multi-digit numbers and multi-letter functions
#     i = 0
#     while i < len(s):
#         c = s[i]
#         # check single character tokens
#         if c in mappings:
#             token_type = mappings[c]
#             token = Node(token_type, c)
#             tokens.append(token)
#             i += 1
#         elif re.match(r'\d', c):
#             j = i
#             while j < len(s) and re.match(r'\d', s[j]):
#                 j += 1
#             token = Node(TokenType.T_NUM, int(s[i:j]))
#             tokens.append(token)
#             i = j
#         elif re.match(r'[a-zA-Z]', c):
#             j = i
#             while j < len(s) and re.match(r'[a-zA-Z]', s[j]):
#                 j += 1
#                 # token = Node(TokenType.T_SIN, s[i:j])
#                 if (s[i:j] in mappings): # if the function is in the mappings
#                     token = Node(mappings[s[i:j]], s[i:j])
#                       # if any that requires parentheses
#                     tokens.append(token)
#                     if (token.token_type == TokenType.T_SIN or token.token_type == TokenType.T_COS or token.token_type == TokenType.T_TAN or token.token_type == TokenType.T_LOG or token.token_type == TokenType.T_SQRT or token.token_type == TokenType.T_SUM or token.token_type == TokenType.T_INTEGRAL or token.token_type == TokenType.T_DERIVATIVE):
#                         if (s[j] != '('):
#                             raise Exception('Invalid syntax on token {}'.format(s[j]) + ', need parentheses with no whitespace after function name')
#                         token.children.append(lexical_analysis(tokens)) # will end on the last parentheses, so dont need to check
#             i = j
#         elif c == ' ' or c == '\t' or c == '\n' or c == '\r':
#             i += 1
#         elif c == ')':
#             return tokens
#         else:
#             raise Exception('Invalid token: {}'.format(c))
#     tokens.append(Node(TokenType.T_END, None))
#     return tokens

# def match(tokens, token):
#     if tokens[0].token_type == token:
#         return tokens.pop(0)
#     else:
#         raise Exception('Invalid syntax on token {}'.format(tokens[0].token_type))

# if __name__ == '__main__':
#     inputstring = 'sin(10*4)'
#     ast = parse(inputstring)
#     print(ast)

class Parser(): 
    # AST parse() throws PLCException

    t = None # current token
    scanner = None # scanner object

    def __init__(self, input):
        self.scanner = Scanner(input)
        # self.scanner.scan(input)

    def consume(self):
        self.t = self.scanner.next()
        return self.t
    
    def isKind(self, kind):
        return self.t.token_type == kind
    
    def match(self, kind):
        if self.isKind(kind):
            return self.consume()
        else:
            raise Exception('Invalid syntax on token {}'.format(self.t.token_type))
        
    def parse(self):
        token = self.consume()
        return self.Equation() # this correct?
    
    # Equation ::= Expression | = Expression
# PowExpr ::= AdditiveExpr ** PowExpr |   AdditiveExpr
# AdditiveExpr ::= MultiplicativeExpr ( ( + | - ) MultiplicativeExpr )*
# MultiplicativeExpr ::= Function (( * | / | % ) Function)*
# Function ::= - | sin(Expression) | cos(Expression) | tan(Expression) | exp(Expression) | log(Expression) | sqrt(Expression) | pi | e | sum(Expression) | mod(Expression) | integral(Expression) | derivative(Expression)
# PrimaryExpr ::= Number ( Expr ) | Z |
# x | y | a | r | inf
# Number ::= [0-9]+ | [0-9]+.[0-9]+ | [0-9]+. | .[0-9]+ | 0. | 0 | 0.0 | 0.0
# Parentheses ::= ( Expression )
# Operation ::= + | - | * | / | ^ | !
# Function ::= sin | cos | tan | exp | log | sqrt | pi | e | sum | mod | integral | derivative Parentheses
        
    def Equation(self):
        if self.isKind(TokenType.T_NUM):
            return self.Expression()
        elif self.isKind(TokenType.T_EQUAL):
            return self.Expression()
        else:
            raise Exception('Invalid syntax on token {}'.format(self.t.token_type))
        
    #         public Expr powExpr() throws SyntaxException, LexicalException
    # {
    #     IToken op = t;
    #     Expr e0 = additiveExpr();

    #     if (isKind(Kind.EXP)) {
    #         op = t;
    #         consume();
    #         Expr e1 = powExpr();
    #         e0 = new BinaryExpr(op, e0, op.getKind(), e1);
    #     }
    #     return e0;
    # }
        
    def Expression(self):
        return self.PowExpr()
    
    def PowExpr(self):
        op = self.t
        e0 = self.AdditiveExpr()

        if self.isKind(TokenType.T_EXP):
            op = self.t
            self.consume()
            e1 = self.PowExpr()
            e0 = PowExpr(op, e0, e1)
        return e0
    
    # AdditiveExpr ::= MultiplicativeExpr ( ( + | - ) MultiplicativeExpr )*
    def AdditiveExpr(self):
        e0 = self.MultiplicativeExpr()
        while self.isKind(TokenType.T_PLUS) or self.isKind(TokenType.T_MINUS):
            op = self.t
            self.consume()
            e1 = self.MultiplicativeExpr()
            e0 = AdditiveExpr(op, e0, e1)
        return e0
    
    # MultiplicativeExpr ::= Function (( * | / | % ) Function)*
    def MultiplicativeExpr(self):
        e0 = self.Function()
        while self.isKind(TokenType.T_MULT) or self.isKind(TokenType.T_DIV) or self.isKind(TokenType.T_MOD):
            op = self.t
            self.consume()
            e1 = self.Function()
            e0 = MultiplicativeExpr(op, e0, e1)
        return e0
    
    # Function ::= - | sin(Expression) | cos(Expression) | tan(Expression) | exp(Expression) | log(Expression) | sqrt(Expression) | pi | e | sum(Expression) | mod(Expression) | integral(Expression) | derivative(Expression)
    def Function(self):
        if self.isKind(TokenType.T_MINUS):
            op = self.t
            self.consume()
            e0 = self.Function()
            return Function(op, e0)
        elif self.isKind(TokenType.T_SIN):
            op = self.t
            self.consume()
            e0 = self.Expression()
            return Function(op, e0)
        elif self.isKind(TokenType.T_COS):
            op = self.t
            self.consume()
            e0 = self.Expression()
            return Function(op, e0)
        elif self.isKind(TokenType.T_TAN):
            op = self.t
            self.consume()
            e0 = self.Expression()
            return Function(op, e0)
        elif self.isKind(TokenType.T_EXP):
            op = self.t
            self.consume()
            e0 = self.Expression()
            return Function(op, e0)
        elif self.isKind(TokenType.T_LOG):
            op = self.t
            self.consume()
            e0 = self.Expression()
            return Function(op, e0)
        elif self.isKind(TokenType.T_SQRT):
            op = self.t
            self.consume()
            e0 = self.Expression()
            return Function(op, e0)
        elif self.isKind(TokenType.T_PI):
            op = self.t
            self.consume()
            return Function(op, None)
        elif self.isKind(TokenType.T_E):
            op = self.t
            self.consume()
            return Function(op, None)
        elif self.isKind(TokenType.T_SUM):
            op = self.t
            self.consume()
            e0 = self.Expression()
            return Function(op, e0)
        elif self.isKind(TokenType.T_MOD):
            op = self.t
            self.consume()
            e0 = self.Expression()
            return Function(op, e0)
        elif self.isKind(TokenType.T_INTEGRAL):
            op = self.t
            self.consume()
            e0 = self.Expression()
            return Function(op, e0)
        elif self.isKind(TokenType.T_DERIVATIVE):
            op = self.t
            self.consume()
            e0 = self.Expression()
            return Function(op, e0)
        else:
            raise Exception('Invalid syntax on token {}'.format(self.t.token_type))
        
    # PrimaryExpr ::= Number ( Expr ) | Z |
    def PrimaryExpr(self):
        if self.isKind(TokenType.T_NUM):
            op = self.t
            self.consume()
            return PrimaryExpr(op, None, None)
        elif self.isKind(TokenType.T_Z):
            op = self.t
            self.consume()
            return PrimaryExpr(op, None, None)
        elif self.isKind(TokenType.T_X):
            op = self.t
            self.consume()
            return PrimaryExpr(op, None, None)
        elif self.isKind(TokenType.T_Y):
            op = self.t
            self.consume()
            return PrimaryExpr(op, None, None)
        elif self.isKind(TokenType.T_A):
            op = self.t
            self.consume()
            return PrimaryExpr(op, None, None)
        elif self.isKind(TokenType.T_R):
            op = self.t
            self.consume()
            return PrimaryExpr(op, None, None)
        elif self.isKind(TokenType.T_INF):
            op = self.t
            self.consume()
            return PrimaryExpr(op, None, None)
        else:
            raise Exception('Invalid syntax on token {}'.format(self.t.token_type))
        
