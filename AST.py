
# public abstract class AST {

# 	public final IToken firstToken;

# 	public AST(IToken firstToken) {
# 		this.firstToken = firstToken;
# 	}

# 	public abstract Object visit(ASTVisitor v, Object arg) throws PLCException;

# 	public IToken getFirstToken() {
# 		return firstToken;
# 	}

# 	public int getLine() {
# 		return firstToken.getSourceLocation().line();
# 	}

# 	public int getColumn() {
# 		return firstToken.getSourceLocation().column();
# 	}

# 	@Override
# 	public int hashCode() {
# 		return Objects.hash(firstToken);
# 	}

# 	@Override
# 	public boolean equals(Object obj) {
# 		if (this == obj)
# 			return true;
# 		if (obj == null)
# 			return false;
# 		if (getClass() != obj.getClass())
# 			return false;
# 		AST other = (AST) obj;
# 		return Objects.equals(firstToken, other.firstToken);
# 	}

# 	@Override
# 	public String toString() {
# 		return "AST [" + (firstToken != null ? "firstToken=" + firstToken : "") + "]";
# 	}

# }

# implement in python

class AST:
    def __init__(self, firstToken):
        self.firstToken = firstToken

    def visit(self, v, arg):
        pass

    def getFirstToken(self):
        return self.firstToken

    def getLine(self):
        return self.firstToken.getSourceLocation().line()

    def getColumn(self):
        return self.firstToken.getSourceLocation().column()

    def __hash__(self):
        return hash(self.firstToken)

    def __eq__(self, obj):
        if self == obj:
            return True
        if obj == None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        return self.firstToken == other.firstToken

    def __str__(self):
        return "AST [" + ("firstToken=" + self.firstToken if self.firstToken != None else "") + "]"