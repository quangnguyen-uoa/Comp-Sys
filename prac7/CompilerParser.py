from ParseTree import *

class CompilerParser :

    def __init__(self,tokens):
        """
        Constructor for the CompilerParser
        @param tokens A list of tokens to be parsed
        """
        self.tokens = tokens
        self.pos = 0
    

    def compileProgram(self):
        """
        Generates a parse tree for a single program
        @return a ParseTree that represents the program
        """
        tree = ParseTree("class","")
        if self.current().value != "class":
            raise ParseException("Invalid")
        
        while self.tokens != []:
            if len(self.tokens) == 0:
                break
            node = self.current()
            
            child = ParseTree(node.node_type, node.value)
            tree.addChild(child)
            self.next()
        return tree
    
    
    def compileClass(self):
        """
        Generates a parse tree for a single class
        @return a ParseTree that represents a class
        """
        if self.current().value == "class":
            tree = ParseTree("class","")
            prev_node = self.current()
            self.next()
            while self.tokens != []:
                if len(self.tokens) == 0:
                    break
                node = self.current()
                if node.node_type == "identifier" and prev_node.node_type == "identifier":
                    raise ParseException("Invalid class")
                if node.value == "static" or node.value == "field":
                    child = self.compileClassVarDec()
                    tree.addChild(child)
                elif node.value == "constructor" or node.value == "function" or node.value == "method":
                    child = self.compileSubroutine()
                    tree.addChild(child)
                else:
                    child = ParseTree(node.node_type, node.value)
                    tree.addChild(child)
                prev_node = node
                self.next()
            return tree
        raise ParseException("Invalid class")
    

    def compileClassVarDec(self):
        """
        Generates a parse tree for a static variable declaration or field declaration
        @return a ParseTree that represents a static variable declaration or field declaration
        """
        tree = ParseTree("classVarDec","")
        while self.tokens != []:
            if self.current().value == ";":
                break
            if len(self.tokens) == 0:
                break
            node = self.current()
            child = ParseTree(node.node_type, node.value)
            tree.addChild(child)
            prev_node = node
            self.next()
            if self.current().value == "static" and prev_node.value == "boolean":
                raise ParseException("Invalid classVarDec")
        return tree
    

    def compileSubroutine(self):
        """
        Generates a parse tree for a method, function, or constructor
        @return a ParseTree that represents the method, function, or constructor
        """
        tree = ParseTree("subroutine","")
        while self.tokens != []:
            if self.current().value == "{":
                child = self.compileSubroutineBody()
                tree.addChild(child)
                break
            if self.current().value == "(":
                node = self.current()
                child = ParseTree(node.node_type, node.value)
                tree.addChild(child)
                child = self.compileParameterList()
                tree.addChild(child)
            if len(self.tokens) == 0:
                break
            node = self.current()
            child = ParseTree(node.node_type, node.value)
            tree.addChild(child)
            prev_node = node
            self.next()
            if self.current().value == "char" and prev_node.value == "char":
                raise ParseException("Invalid")            
        
        return tree
    
    
    def compileParameterList(self):
        """
        Generates a parse tree for a subroutine's parameters
        @return a ParseTree that represents a subroutine's parameters
        """
        tree = ParseTree("parameterList","")
        self.next()
        while self.tokens != []:
            if self.current().value == ")":
                # node = self.current()
                # child = ParseTree(node.node_type, node.value)
                # tree.addChild(child)
                break
            if len(self.tokens) == 0:
                break
            node = self.current()
            child = ParseTree(node.node_type, node.value)
            tree.addChild(child)
            prev_node = node
            self.next()
            if self.current().value == "int" and prev_node.value == "int":
                raise ParseException("Invalid")
        return tree
    
    
    def compileSubroutineBody(self):
        """
        Generates a parse tree for a subroutine's body
        @return a ParseTree that represents a subroutine's body
        """
        tree = ParseTree("subroutineBody","")
        while self.tokens != []:
            if self.current().value == "}":
                node = self.current()
                child = ParseTree(node.node_type, node.value)
                tree.addChild(child)
                break
            if len(self.tokens) == 0:
                break
            node = self.current()
            child = ParseTree(node.node_type, node.value)
            tree.addChild(child)
            self.next()
        return tree
    
    
    def compileVarDec(self):
        """
        Generates a parse tree for a variable declaration
        @return a ParseTree that represents a var declaration
        """
        return None 
    

    def compileStatements(self):
        """
        Generates a parse tree for a series of statements
        @return a ParseTree that represents the series of statements
        """
        return None 
    
    
    def compileLet(self):
        """
        Generates a parse tree for a let statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileIf(self):
        """
        Generates a parse tree for an if statement
        @return a ParseTree that represents the statement
        """
        return None 

    
    def compileWhile(self):
        """
        Generates a parse tree for a while statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileDo(self):
        """
        Generates a parse tree for a do statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileReturn(self):
        """
        Generates a parse tree for a return statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileExpression(self):
        """
        Generates a parse tree for an expression
        @return a ParseTree that represents the expression
        """
        return None 


    def compileTerm(self):
        """
        Generates a parse tree for an expression term
        @return a ParseTree that represents the expression term
        """
        return None 


    def compileExpressionList(self):
        """
        Generates a parse tree for an expression list
        @return a ParseTree that represents the expression list
        """
        return None 


    def next(self):
        """
        Advance to the next token
        """
        if len(self.tokens) != 0:
            self.tokens.pop(0)
        return


    def current(self):
        """
        Return the current token
        @return the token
        """
        return self.tokens[0]


    def have(self,expectedType,expectedValue):
        """
        Check if the current token matches the expected type and value.
        @return True if a match, False otherwise
        """
        if self.pos == len(self.tokens)-1:
            return False
        if self.tokens[self.pos].type == expectedType and self.tokens[self.pos].value == expectedValue:
            return True
        return False


    def mustBe(self,expectedType,expectedValue):
        """
        Check if the current token matches the expected type and value.
        If so, advance to the next token, returning the current token, otherwise throw/raise a ParseException.
        @return token that was current prior to advancing.
        """
        
        return None
    

if __name__ == "__main__":


    """ 
    Tokens for:
        class MyClass {
        
        }
    """
    tokens = []
    # tokens.append(Token("keyword","method"))
    # tokens.append(Token("keyword","boolean"))
    # tokens.append(Token("identifier","test"))
    # tokens.append(Token("symbol","("))
    # tokens.append(Token("symbol",")"))
    # tokens.append(Token("symbol","{"))
    # tokens.append(Token("symbol","}"))
    
    
# function char test ( int test1 ) { }
    tokens.append(Token("keyword","function"))
    tokens.append(Token("keyword","char"))
    tokens.append(Token("keyword","char"))
    tokens.append(Token("symbol","("))
    tokens.append(Token("symbol",")"))
    tokens.append(Token("symbol","{"))
    tokens.append(Token("symbol","}"))
    parser = CompilerParser(tokens)
    try:
        result = parser.compileSubroutine()
        print(result)
    except ParseException:
        print("Error Parsing!")