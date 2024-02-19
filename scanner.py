# package edu.ufl.cise.plcsp23;

# import java.util.Arrays;
# import java.util.HashMap;

# public class Scanner implements IScanner {

#     final String input;
#     //array containing input chars, terminated with extra char 0
#     final char[] inputChars;

#     //invariant ch == inputChars[pos]
#     int pos; //position of ch
#     char ch; //next char
#     private static HashMap<String, Token.Kind> operatorOrSeparator;

#     /*		IDENT,
# 		NUM_LIT,
# 		STRING_LIT,
# 		RES_image,
# 		RES_pixel,
# 		RES_int,
# 		RES_string,
# 		RES_void,
# 		RES_nil,
# 		RES_load,
# 		RES_display,
# 		RES_write,
# 		RES_x,
# 		RES_y,
# 		RES_a,
# 		RES_r,
# 		RES_X,
# 		RES_Y,
# 		RES_Z,
# 		RES_x_cart,
# 		RES_y_cart,
# 		RES_a_polar,
# 		RES_r_polar,
# 		RES_rand,
# 		RES_sin,
# 		RES_cos,
# 		RES_atan,
# 		RES_if,
# 		RES_while,
# 		DOT, //  .
# 		COMMA, // ,
# 		QUESTION, // ?
# 		COLON, // :
# 		LPAREN, // (
# 		RPAREN, // )
# 		LT, // <
# 		GT, // >
# 		LSQUARE, // [
# 		RSQUARE, // ]
# 		LCURLY, // {
# 		RCURLY, // }
# 		ASSIGN, // =
# 		EQ, // ==
# 		EXCHANGE, // <->
# 		LE, // <=
# 		GE, // >=
# 		BANG, // !
# 		BITAND, // &
# 		AND, // &&
# 		BITOR, // |
# 		OR, // ||
# 		PLUS, // +
# 		MINUS, // -
# 		TIMES, // *
# 		EXP, // **
# 		DIV, // /
# 		MOD, // %
# 		EOF,
# 		ERROR,
# 		RES_red,
# 		RES_grn,
# 		RES_blu */
#     static {
#         operatorOrSeparator = new HashMap<String,Token.Kind>();
#         operatorOrSeparator.put(".", Token.Kind.DOT);
#         operatorOrSeparator.put(",", Token.Kind.COMMA);
#         operatorOrSeparator.put("?", Token.Kind.QUESTION);
#         operatorOrSeparator.put(":", Token.Kind.COLON);
#         operatorOrSeparator.put("(", Token.Kind.LPAREN);
#         operatorOrSeparator.put(")", Token.Kind.RPAREN);
#         operatorOrSeparator.put("<", Token.Kind.LT);
#         operatorOrSeparator.put(">", Token.Kind.GT);
#         operatorOrSeparator.put("[", Token.Kind.LSQUARE);
#         operatorOrSeparator.put("]", Token.Kind.RSQUARE);
#         operatorOrSeparator.put("{", Token.Kind.LCURLY);
#         operatorOrSeparator.put("}", Token.Kind.RCURLY);
#         operatorOrSeparator.put("=", Token.Kind.ASSIGN);
#         operatorOrSeparator.put("==", Token.Kind.EQ);
#         operatorOrSeparator.put("<->", Token.Kind.EXCHANGE);
#         operatorOrSeparator.put("<=", Token.Kind.LE);
#         operatorOrSeparator.put(">=", Token.Kind.GE);
#         operatorOrSeparator.put("!", Token.Kind.BANG);
#         operatorOrSeparator.put("&", Token.Kind.BITAND); 
#         operatorOrSeparator.put("&&", Token.Kind.AND);
#         operatorOrSeparator.put("|", Token.Kind.BITOR);
#         operatorOrSeparator.put("||", Token.Kind.OR);
#         operatorOrSeparator.put("+", Token.Kind.PLUS);
#         operatorOrSeparator.put("-", Token.Kind.MINUS);
#         operatorOrSeparator.put("*", Token.Kind.TIMES);
#         operatorOrSeparator.put("**", Token.Kind.EXP);
#         operatorOrSeparator.put("/", Token.Kind.DIV);
#         operatorOrSeparator.put("%", Token.Kind.MOD);
#         operatorOrSeparator.put("void", Token.Kind.RES_void);
#         operatorOrSeparator.put("int", Token.Kind.RES_int);
#         operatorOrSeparator.put("string", Token.Kind.RES_string);
#         operatorOrSeparator.put("image", Token.Kind.RES_image);
#         operatorOrSeparator.put("pixel", Token.Kind.RES_pixel);
#         operatorOrSeparator.put("nil", Token.Kind.RES_nil);
#         operatorOrSeparator.put("load", Token.Kind.RES_load);
#         operatorOrSeparator.put("display", Token.Kind.RES_display);
#         operatorOrSeparator.put("write", Token.Kind.RES_write);
#         operatorOrSeparator.put("x", Token.Kind.RES_x);
#         operatorOrSeparator.put("y", Token.Kind.RES_y);
#         operatorOrSeparator.put("a", Token.Kind.RES_a);
#         operatorOrSeparator.put("r", Token.Kind.RES_r);
#         operatorOrSeparator.put("X", Token.Kind.RES_X);
#         operatorOrSeparator.put("Y", Token.Kind.RES_Y);
#         operatorOrSeparator.put("Z", Token.Kind.RES_Z);
#         operatorOrSeparator.put("x_cart", Token.Kind.RES_x_cart);
#         operatorOrSeparator.put("y_cart", Token.Kind.RES_y_cart);
#         operatorOrSeparator.put("a_polar", Token.Kind.RES_a_polar);
#         operatorOrSeparator.put("r_polar", Token.Kind.RES_r_polar);
#         operatorOrSeparator.put("rand", Token.Kind.RES_rand);
#         operatorOrSeparator.put("sin", Token.Kind.RES_sin);
#         operatorOrSeparator.put("cos", Token.Kind.RES_cos);
#         operatorOrSeparator.put("atan", Token.Kind.RES_atan);
#         operatorOrSeparator.put("if", Token.Kind.RES_if);
#         operatorOrSeparator.put("while", Token.Kind.RES_while);
#         operatorOrSeparator.put("red", Token.Kind.RES_red);
#         operatorOrSeparator.put("grn", Token.Kind.RES_grn);
#         operatorOrSeparator.put("blu", Token.Kind.RES_blu);
#     }

#     private enum State {
#         START, 
#         IN_IDENT, 
#         IN_NUM_LIT, 
#         HAVE_EQ,
#         COMMENT,
#         IN_STRING_LIT,
#     }

#     // Utility Functions
#     private boolean isDigit(int ch) {
#         return '0' <= ch && ch <= '9';
#     }

#     private boolean isLetter(int ch) {
#         return ('A' <= ch && ch <= 'Z') || ('a' <= ch && ch <= 'z');
#     }

#     private boolean isWhiteSpace(int ch) {
#         return ch == ' ' || ch == '\n' || ch == '\r' || ch == '\t' || ch == '\f';
#     }
    
#     //constructor
#     public Scanner(String input) {
#         this.input = input;
#         inputChars = Arrays.copyOf(input.toCharArray(), input.length() + 1);
#         pos = 0;
#         ch = inputChars[pos];
#     }

#     @Override
#     public IToken next() throws LexicalException {
#         return scanToken();
#     }

#     private void nextChar() {
#         pos++;
#         if (pos >= inputChars.length) {
#           ch = 0; 
#           // set ch to the end of input character
#         } else {
#           ch = inputChars[pos];
#         }          
#     }

#     private IToken scanToken() throws LexicalException {
#         State state = State.START;
#         int tokenStart = -1;

#         while(true) { 
#             //read chars, loop terminates when a Token is returned             
#             switch(state) {
#                 case START: {
#                     tokenStart = pos;
#                     switch(ch) {
#                         // end of input
#                         case 0: 
#                             return new Token(Token.Kind.EOF, tokenStart, 0, inputChars);
#                         // handle white space, new line, tab, etc.
#                         case ' ','\n','\r','\t','\f':
#                             nextChar(); 
#                             continue;
#                         case '.':
#                             nextChar();
#                             return new Token(Token.Kind.DOT, tokenStart, 1, inputChars);
#                         case ',':
#                             nextChar();
#                             return new Token(Token.Kind.COMMA, tokenStart, 1, inputChars);
#                         case '?':
#                             nextChar();
#                             return new Token(Token.Kind.QUESTION, tokenStart, 1, inputChars);
#                         case ':':
#                             nextChar();
#                             return new Token(Token.Kind.COLON, tokenStart, 1, inputChars);
#                         case '(':
#                             nextChar();
#                             return new Token(Token.Kind.LPAREN, tokenStart, 1, inputChars);
#                         case ')':
#                             nextChar();
#                             return new Token(Token.Kind.RPAREN, tokenStart, 1, inputChars);
#                         case '<':
#                             nextChar();
#                             if (ch == '-') {
#                                 nextChar();
#                                 if (ch == '>') {
#                                     nextChar();
#                                     return new Token(Token.Kind.EXCHANGE, tokenStart, 3, inputChars);
#                                 }
#                                 else {
#                                     throw new LexicalException(
#                                         "Illegal Exchange" );
#                                 }
                            
#                             }
#                             else if (ch == '=') {
#                                 nextChar();
#                                 return new Token(Token.Kind.LE, tokenStart, 2, inputChars);
#                             }
#                             else {
#                                 return new Token(Token.Kind.LT, tokenStart, 1, inputChars);
#                             }
#                         case '>':
#                             nextChar();
#                             if (ch == '=') {
#                                 nextChar();
#                                 return new Token(Token.Kind.GE, tokenStart, 2, inputChars);
#                             }
#                             return new Token(Token.Kind.GT, tokenStart, 1, inputChars);
#                         case '[':
#                             nextChar();
#                             return new Token(Token.Kind.LSQUARE, tokenStart, 1, inputChars);
#                         case ']':
#                             nextChar();
#                             return new Token(Token.Kind.RSQUARE, tokenStart, 1, inputChars);
#                         case '{':
#                             nextChar();
#                             return new Token(Token.Kind.LCURLY, tokenStart, 1, inputChars);
#                         case '}':
#                             nextChar();
#                             return new Token(Token.Kind.RCURLY, tokenStart, 1, inputChars);
#                         case '=': 
#                             state = State.HAVE_EQ;
#                             nextChar();
#                             continue;
#                         case '!':
#                             nextChar();
#                             return new Token(Token.Kind.BANG, tokenStart, 1, inputChars);
#                         case '&':
#                             nextChar();
#                             if (ch == '&') {
#                                 nextChar();
#                                 return new Token(Token.Kind.AND, tokenStart, 2, inputChars);
#                             }
#                             return new Token(Token.Kind.BITAND, tokenStart, 1, inputChars);
#                         case '|':
#                             nextChar();
#                             if (ch == '|') {
#                                 nextChar();
#                                 return new Token(Token.Kind.OR, tokenStart, 2, inputChars);
#                             }
#                             return new Token(Token.Kind.BITOR, tokenStart, 1, inputChars);
#                         case '+':
#                             nextChar();
#                             return new Token(Token.Kind.PLUS, tokenStart, 1, inputChars);
#                         case '-':
#                             nextChar();
#                             return new Token(Token.Kind.MINUS, tokenStart, 1, inputChars);
#                         case '*': 
#                             nextChar();
#                             if (ch == '*') {
#                                 nextChar();
#                                 return new Token(Token.Kind.EXP, tokenStart, 2, inputChars);
#                             }
#                             return new Token(Token.Kind.TIMES, tokenStart, 1, inputChars);
#                         case '/':
#                             nextChar();
#                             return new Token(Token.Kind.DIV, tokenStart, 1, inputChars);
#                         case '%':
#                             nextChar();
#                             return new Token(Token.Kind.MOD, tokenStart, 1, inputChars);
#                         // check for string lit
#                         case '"':
#                             state = State.IN_STRING_LIT;
#                             nextChar();
#                             continue;
#                         case '0': 
#                             nextChar();
#                             return new Token(Token.Kind.NUM_LIT, tokenStart, 1, inputChars);
#                         case '1', '2', '3', '4', '5', '6', '7', '8', '9':
#                             state = State.IN_NUM_LIT;
#                             nextChar();
#                             continue;
#                         // isIdentStart does not work with case since it returns a boolean
#                         case 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','$': // all possible starts to in_ident
#                             state = State.IN_IDENT;
#                             nextChar();
#                             continue;
#                         case '~':
#                             nextChar();
#                             state = State.COMMENT;
#                             continue;
#                         default: 
#                             // once all is implemented, should just be Not(a..z,A..Z,$,_,0..9, +,*,=)
#                             throw new LexicalException(
#                                 "Not a valid character" 
#                             );
#                     }
#                 }
#                 case HAVE_EQ: {
#                     if (ch == '=') {
#                         nextChar();
#                         return new Token(Token.Kind.EQ, tokenStart, 2, inputChars);
#                     } 
#                     else {
#                         return new Token(Token.Kind.ASSIGN, tokenStart, 1, inputChars);
#                     }

#                 }
#                 case IN_NUM_LIT: {
#                     if (isDigit(ch)) {
#                         nextChar();
#                     } else {
#                         int length = pos - tokenStart;
#                         state = State.START; 
#                         return new Token(Token.Kind.NUM_LIT, tokenStart, length, inputChars);
#                     }
#                     continue;
#                 }
#                 case IN_IDENT: {
#                     switch (ch) {
#                         // all possible continuations of in_ident, now including digits
#                         case 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','$','0','1','2','3','4','5','6','7','8','9': 
#                             nextChar();
#                             continue;
#                         default: {
#                             int length = pos - tokenStart;
#                             state = State.START; // need to reset state after token is found
#                             return new Token(Token.Kind.IDENT, tokenStart, length, inputChars);
#                         }
#                     }
#                 }
#                 case COMMENT: {
#                     switch (ch) {
#                         case '\n':
#                             nextChar();
#                             state = State.START;
#                             continue;
#                         default:
#                             nextChar();
#                             continue;
#                     }
#                 }
#                 case IN_STRING_LIT:
#                     switch (ch) {
#                         case 0:
#                             throw new LexicalException("Illegal character in string lit, EOF, invalid post-\\: " + pos);
#                         case '"':
#                             nextChar();
#                             state = State.START;
#                             return new StringToken(Token.Kind.STRING_LIT, tokenStart, pos - tokenStart, inputChars);
#                             // continue;
#                         case '\\':
#                             nextChar();
#                             switch (ch) {
#                                 case 'b':
#                                     nextChar();
#                                     continue;
#                                 case 't':
#                                     nextChar();
#                                     continue;
#                                 case 'n':
#                                     nextChar();
#                                     continue;
#                                 case 'r':
#                                     nextChar();
#                                     continue;
#                                 case '\"':
#                                     nextChar();
#                                     continue;
#                                 case '\\':
#                                     nextChar();
#                                     continue;
#                                 default:
#                                     throw new LexicalException("Illegal character in string lit, invalid post-\\: " + pos);
#                             }
#                         case '\n', '\r': 
#                             // make own tests for these !!!??? '\t', '\b', '\f' // these are illegal in string lit
#                             throw new LexicalException("Illegal character in string lit, newline: " + pos);
                        
#                         default:
#                             nextChar();
#                             continue;
#                     }

                    
#                 default: {
#                     // could also change to "not implemented yet", as suggested in the slides
#                     throw new UnsupportedOperationException("Bug in Scanner");
#                 }
#             }
#         }
#     }
# }

# create the above implementation for a scanner in python
# with the syntax:
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
        
class Scanner():
    # final String input;
    input = ""
    # char ch
    ch = ""
    pos = 0 # position of ch

    # State enum
    class State:
        START = 0
        IN_IDENT = 1
        IN_NUM_LIT = 2
        HAVE_EQ = 3
        COMMENT = 4
        IN_STRING_LIT = 5
    
    def isDigit(self, ch):
        return '0' <= ch and ch <= '9'
    
    def Scanner(self, input):
        self.input = input
        self.ch = self.input[self.pos]

    # @Override
    # public IToken next() throws LexicalException {
    #     return scanToken();
    # }
    def next(self):
        return self.scanToken()
    
    def nextChar(self):
        self.pos += 1
        if self.pos >= len(self.input):
            self.ch = 0
        else:
            self.ch = self.input[self.pos]

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
        
    def scanToken(self):
        state = self.State.START
        tokenStart = -1

        while True:
            # switch(state) { python does not have switch case, so we will use if else
            match state:
                case self.State.START:
                    tokenStart = self.pos

                    match(self.ch):
                        case 0:
                            return Token(Token.Kind.END, tokenStart, 0, self.input)
