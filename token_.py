# package edu.ufl.cise.plcsp23;
# import java.util.HashMap;
# import java.util.function.Function;

# public class Token implements INumLitToken {

#     final Kind kind;
#     final int pos;
#     final int length;
#     final char[] source;
#     final int value;
#     final int tokenLine;
#     final int tokenColumn;
#     private static HashMap<String, Kind> reservedWords;

#     static {
#         reservedWords = new HashMap<String,Kind>();
#         reservedWords.put(".", Token.Kind.DOT);
#         reservedWords.put(",", Token.Kind.COMMA);
#         reservedWords.put("?", Token.Kind.QUESTION);
#         reservedWords.put(":", Token.Kind.COLON);
#         reservedWords.put("(", Token.Kind.LPAREN);
#         reservedWords.put(")", Token.Kind.RPAREN);
#         reservedWords.put("<", Token.Kind.LT);
#         reservedWords.put(">", Token.Kind.GT);
#         reservedWords.put("[", Token.Kind.LSQUARE);
#         reservedWords.put("]", Token.Kind.RSQUARE);
#         reservedWords.put("{", Token.Kind.LCURLY);
#         reservedWords.put("}", Token.Kind.RCURLY);
#         reservedWords.put("=", Token.Kind.ASSIGN);
#         reservedWords.put("==", Token.Kind.EQ);
#         reservedWords.put("<->", Token.Kind.EXCHANGE);
#         reservedWords.put("<=", Token.Kind.LE);
#         reservedWords.put(">=", Token.Kind.GE);
#         reservedWords.put("!", Token.Kind.BANG);
#         reservedWords.put("&", Token.Kind.BITAND); 
#         reservedWords.put("&&", Token.Kind.AND);
#         reservedWords.put("|", Token.Kind.BITOR);
#         reservedWords.put("||", Token.Kind.OR);
#         reservedWords.put("+", Token.Kind.PLUS);
#         reservedWords.put("-", Token.Kind.MINUS);
#         reservedWords.put("*", Token.Kind.TIMES);
#         reservedWords.put("**", Token.Kind.EXP);
#         reservedWords.put("/", Token.Kind.DIV);
#         reservedWords.put("%", Token.Kind.MOD);
#         reservedWords.put("void", Token.Kind.RES_void);
#         reservedWords.put("int", Token.Kind.RES_int);
#         reservedWords.put("string", Token.Kind.RES_string);
#         reservedWords.put("image", Token.Kind.RES_image);
#         reservedWords.put("pixel", Token.Kind.RES_pixel);
#         reservedWords.put("nil", Token.Kind.RES_nil);
#         reservedWords.put("load", Token.Kind.RES_load);
#         reservedWords.put("display", Token.Kind.RES_display);
#         reservedWords.put("write", Token.Kind.RES_write);
#         reservedWords.put("x", Token.Kind.RES_x);
#         reservedWords.put("y", Token.Kind.RES_y);
#         reservedWords.put("a", Token.Kind.RES_a);
#         reservedWords.put("r", Token.Kind.RES_r);
#         reservedWords.put("X", Token.Kind.RES_X);
#         reservedWords.put("Y", Token.Kind.RES_Y);
#         reservedWords.put("Z", Token.Kind.RES_Z);
#         reservedWords.put("x_cart", Token.Kind.RES_x_cart);
#         reservedWords.put("y_cart", Token.Kind.RES_y_cart);
#         reservedWords.put("a_polar", Token.Kind.RES_a_polar);
#         reservedWords.put("r_polar", Token.Kind.RES_r_polar);
#         reservedWords.put("rand", Token.Kind.RES_rand);
#         reservedWords.put("sin", Token.Kind.RES_sin);
#         reservedWords.put("cos", Token.Kind.RES_cos);
#         reservedWords.put("atan", Token.Kind.RES_atan);
#         reservedWords.put("if", Token.Kind.RES_if);
#         reservedWords.put("while", Token.Kind.RES_while);
#         reservedWords.put("red", Token.Kind.RES_red);
#         reservedWords.put("grn", Token.Kind.RES_grn);
#         reservedWords.put("blu", Token.Kind.RES_blu);
#     }

#     public Token(Kind kind, int pos, int length, char[] source) throws LexicalException {
#         super();
#         this.pos = pos;
#         this.length = length;
#         this.source = source;

#         if (kind == Kind.IDENT) {
#             String s = new String(source, pos, length);
#             if (reservedWords.containsKey(s)) {
#                 this.kind = reservedWords.get(s);
#             }
#             else {
#                 this.kind = kind;
#             }
#         }
#         else
#             this.kind = kind;
        
        
#         if (kind == Kind.NUM_LIT) {
#             try {
#                 value = Integer.parseInt(new String(source, pos, length));
                
#             } catch (Exception e) {
#                 throw new LexicalException("Invalid number literal, position:" + pos);
#             }
#         }
#         else {
#             value = 0;
#         }

#         int line = 1;
#         int lastNewLine = 0;
#         for (int i = 0; i < pos; i++) {
#             if (source[i] == '\n') {
#                 line++;
#                 lastNewLine = i + 1;
#             }
#         }
#         tokenLine = line;
#         tokenColumn = pos - lastNewLine + 1;
#     }

#     public SourceLocation getSourceLocation() {
#         return new SourceLocation(tokenLine, tokenColumn);
#     }

#     public Kind getKind() {
#         return kind;
#     }

#     //returns the value of the token if it is a number literal
#     @Override
#     public int getValue() {
#         return value; 
#     }

    
#     //returns the characters from the source belonging to the token
#     public String getTokenString() {
#         return new String(source, pos, length); //new String(kind, pos, length, source);    // ???
#     }  

#     //prints token, used during development
#     @Override  
#     public String toString() {
#         return getTokenString();
#     } 
# }

# implement in python for grammar 
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
        
# kind
class Kind():
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
    #     public Token(Kind kind, int pos, int length, char[] source) throws LexicalException {
    kind = None
    pos = None
    length = None
    source = None
    value = None
    tokenLine = None
    tokenColumn = None
    reservedWords = None

    def __init__(self, kind, pos, length, source):
        self.kind = kind
        self.pos = pos
        self.length = length
        self.source = source
        self.value = 0
        self.tokenLine = 0
        self.tokenColumn = 0
        
        # no idents

        line = 1
        lastNewLine = 0
        for i in range(pos):
            if source[i] == '\n':
                line += 1
                lastNewLine = i + 1
        self.tokenLine = line
        self.tokenColumn = pos - lastNewLine + 1

    def getSourceLocation(self):
        return [self.tokenLine, self.tokenColumn]
    
    def getKind(self):
        return self.kind
    
    def getValue(self):
        return self.value
    
    def getTokenString(self):
        return ''.join(self.source[self.pos:self.pos+self.length])
    
    def __str__(self):
        return self.getTokenString()