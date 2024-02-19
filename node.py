class Node:
    def __init__(self, token_type):
        self.token_type = token_type
        
# extends in Python 
class Equation(Node):
    def __init__(self, token_type, left, right):
        super().__init__(token_type)
        self.left, self.right = left, right
    
class PowExpr(Node):
    def __init__(self, token_type, left, right):
        super().__init__(token_type)
        self.left, self.right = left, right

class AdditiveExpr(Node):
    def __init__(self, token_type, left, right):
        super().__init__(token_type)
        self.left, self.right = left, right

class MultiplicativeExpr(Node):
    def __init__(self, token_type, left, right):
        super().__init__(token_type)
        self.left, self.right = left, right

class Function(Node):
    def __init__(self, token_type, expr):
        super().__init__(token_type)
        self.expr = expr
        
class PrimaryExpr(Node):
    def __init__(self, token_type, left, right):
        super().__init__(token_type)
        self.left, self.right = left, right

class Number(Node):
    def __init__(self, token_type, value):
        super().__init__(token_type)
        self.value = value

class Parentheses(Node):
    def __init__(self, token_type, expr):
        super().__init__(token_type)
        self.expr = expr