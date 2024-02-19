# create a parser for math expressions that uses numpy
import numpy as np
import enum
import math
import re
import sys
import argparse

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

class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []

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

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

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

def lexical_analysis(s):
    mappings = {
        '+': TokenType.T_PLUS,
        '-': TokenType.T_MINUS,
        '*': TokenType.T_MULT,
        '/': TokenType.T_DIV,
        '(': TokenType.T_LPAR,
        ')': TokenType.T_RPAR,
        '^': TokenType.T_EXP,
        '!': TokenType.T_FACT
    }

    tokens = []
    # for c in s:
    #     if c in mappings:
    #         token_type = mappings[c]
    #         token = Node(token_type, value=c)
    #     elif re.match(r'\d', c):  
    #         token = Node(TokenType.T_NUM, value=int(c))
    #     # ignore whitespace
    #     elif c == ' ' or c == '\t' or c == '\n' or c == '\r':
    #         continue
    #     else:
    #         raise Exception('Invalid token: {}'.format(c))
    #     tokens.append(token)
    # tokens.append(Node(TokenType.T_END))
    # return tokens

    # change to work for multi-digit numbers and multi-letter functions
    i = 0
    while i < len(s):
        c = s[i]
        if c in mappings:
            token_type = mappings[c]
            token = Token(token_type, c)
            tokens.append(token)
            i += 1
        elif re.match(r'\d', c):
            j = i
            while j < len(s) and re.match(r'\d', s[j]):
                j += 1
            token = Token(TokenType.T_NUM, int(s[i:j]))
            tokens.append(token)
            i = j
        elif re.match(r'[a-zA-Z]', c):
            j = i
            while j < len(s) and re.match(r'[a-zA-Z]', s[j]):
                j += 1
            token = Token(TokenType.T_SIN, s[i:j])
            tokens.append(token)
            i = j
        elif c == ' ' or c == '\t' or c == '\n' or c == '\r':
            i += 1
        else:
            raise Exception('Invalid token: {}'.format(c))

def match(tokens, token):
    if tokens[0].token_type == token:
        return tokens.pop(0)
    else:
        raise Exception('Invalid syntax on token {}'.format(tokens[0].token_type))


def parse_e(tokens):
    left_node = parse_e2(tokens)

    while tokens[0].token_type in [TokenType.T_PLUS, TokenType.T_MINUS]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e2(tokens))
        left_node = node

    return left_node

def parse_e2(tokens):
    left_node = parse_e3(tokens)

    while tokens[0].token_type in [TokenType.T_MULT, TokenType.T_DIV]:
        node = tokens.pop(0)
        node.children.append(left_node)
        node.children.append(parse_e3(tokens))
        left_node = node

    return left_node


def parse_e3(tokens):
    # if tokens[0].token_type == TokenType.T_NUM:
    #     return tokens.pop(0)
    # rewrite so it doesnt throw an error when null
    if len(tokens) == 0:
        return None
    elif tokens[0].token_type == TokenType.T_NUM:
        return tokens.pop(0)

    match(tokens, TokenType.T_LPAR)
    expression = parse_e(tokens)
    match(tokens, TokenType.T_RPAR)

    return expression


def parse(inputstring):
    tokens = lexical_analysis(inputstring)
    ast = parse_e(tokens)
    match(tokens, TokenType.T_END)
    return ast

if __name__ == '__main__':
    inputstring = '23 * (3 + 4)'
    ast = parse(inputstring)
    print(ast)




