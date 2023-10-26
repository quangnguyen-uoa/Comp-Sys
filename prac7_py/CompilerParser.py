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
        # if self.mustBe("keyword","class"):
        #     tree = self.compileClass()
        # else:
        #     raise ParseException("Invalid")
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
            while self.tokens != []:
                if len(self.tokens) == 0:
                    break
                node = self.current()
                if node.value == "static" or node.value == "field":
                    child = self.compileClassVarDec()
                    tree.addChild(child)
                elif node.value == "constructor" or node.value == "function" or node.value == "method":
                    child = self.compileSubroutine()
                    tree.addChild(child)
                else:
                    raise ParseException("Invalid class variable declaration or subroutine")
                self.next()
                
            # tree.addChild(self.mustBe("keyword","class"))
            # tree.addChild(self.mustBe("identifier",""))
            # tree.addChild(self.mustBe("symbol","{"))
            # while self.have("keyword", ""):
            #     if self.have("keyword", "static") or self.have("keyword", "field"):
            #         tree.addChild(self.compileClassVarDec())
            #     elif self.have("keyword", "constructor") or self.have("keyword", "function") or self.have("keyword", "method"):
            #         tree.addChild(self.compileSubroutine())
            #     else:
            #         raise ParseException("Invalid class variable declaration or subroutine")
            # tree.addChild(self.mustBe("symbol","}"))
            return tree
        raise ParseException("Invalid class")
    

    def compileClassVarDec(self):
        """
        Generates a parse tree for a static variable declaration or field declaration
        @return a ParseTree that represents a static variable declaration or field declaration
        """
        # tree = ParseTree("classVarDec","")
        # tree.addChild(self.mustBe("keyword","static") or self.mustBe("keyword","field"))
        # tree
        return None 
    

    def compileSubroutine(self):
        """
        Generates a parse tree for a method, function, or constructor
        @return a ParseTree that represents the method, function, or constructor
        """
        return None 
    
    
    def compileParameterList(self):
        """
        Generates a parse tree for a subroutine's parameters
        @return a ParseTree that represents a subroutine's parameters
        """
        return None 
    
    
    def compileSubroutineBody(self):
        """
        Generates a parse tree for a subroutine's body
        @return a ParseTree that represents a subroutine's body
        """
        return None 
    
    
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
    tokens.append(Token("keyword","class"))
    tokens.append(Token("identifier","MyClass"))
    tokens.append(Token("symbol","{"))
    tokens.append(Token("symbol","}"))

    parser = CompilerParser(tokens)
    try:
        result = parser.compileProgram()
        print(result)
    except ParseException:
        print("Error Parsing!")