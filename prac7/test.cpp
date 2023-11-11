/**
 * Generates a parse tree for an expression
 * @return a ParseTree
 */
ParseTree* CompilerParser::compileExpression() {
    ParseTree* expression = new ParseTree("expression", "");
    
    if (have("keyword", "skip")) {
        expression->addChild(mustBe("keyword", "skip"));
    } else {
        expression->addChild(compileTerm());
        while (have("symbol", "") && isOperator(current()->getValue())) {
            expression->addChild(new ParseTree(current()->getType(), current()->getValue()));  
            next();
            expression->addChild(compileTerm());
        }
    }
    return expression;
}

// Helper method to check if a symbol is a valid operator
bool CompilerParser::isOperator(const std::string& symbol) {
    return symbol == "+" || symbol == "-" || symbol == "*" || symbol == "/" || 
           symbol == "&" || symbol == "|" || symbol == "<" || symbol == ">" || symbol == "=";
}

/**
 * Generates a parse tree for an expression term
 * @return a ParseTree
 */
ParseTree* CompilerParser::compileTerm() {
    ParseTree* term = new ParseTree("term", "");
    if (have("integerConstant", "") || have("stringConstant", "") || have("keyword", "true") || 
        have("keyword", "false") || have("keyword", "null") || have("keyword", "this")) {
        term->addChild(new ParseTree(current()->getType(), current()->getValue()));
        next();
    } else if (have("identifier", "")) {
        term->addChild(mustBe("identifier", ""));  // Expect 'varName'
        if (have("symbol", "[")) {
            term->addChild(mustBe("symbol", "["));
            term->addChild(compileExpression());
            term->addChild(mustBe("symbol", "]"));
        } else if (have("symbol", "(")) {
            term->addChild(mustBe("symbol", "("));
            term->addChild(compileExpressionList());
            term->addChild(mustBe("symbol", ")"));
        } else if (have("symbol", ".")) {
            term->addChild(mustBe("symbol", "."));
            term->addChild(mustBe("identifier", ""));  // Expect 'subroutineName'
            term->addChild(mustBe("symbol", "("));
            term->addChild(compileExpressionList());
            term->addChild(mustBe("symbol", ")"));
        }
    } else if (have("symbol", "(")) {
        term->addChild(mustBe("symbol", "("));
        term->addChild(compileExpression());
        term->addChild(mustBe("symbol", ")"));
    } else if (have("symbol", "-") || have("symbol", "~")) {
        term->addChild(new ParseTree(current()->getType(), current()->getValue()));
        next();
        term->addChild(compileTerm());
    } else {
        throw ParseException();
    }
    return term;
}

/**
 * Generates a parse tree for an expression list
 * @return a ParseTree
 */
ParseTree* CompilerParser::compileExpressionList() {
    ParseTree* expressionList = new ParseTree("expressionList", "");
    if (have("symbol", ")")) {
        return expressionList;
    }

    expressionList->addChild(compileExpression());
    while (have("symbol", ",")) {
        expressionList->addChild(mustBe("symbol", ","));
        expressionList->addChild(compileExpression());
    }
    return expressionList;
}

/**
 * Generates a parse tree for a subroutine call
 * @return a ParseTree
 */
ParseTree* CompilerParser::compileSubroutineCall() {
    ParseTree* subroutineCall = new ParseTree("subroutineCall", "");
    subroutineCall->addChild(mustBe("identifier", ""));  // Expect subroutineName or className or varName
    
    // subroutineName '(' expressionList ')'
    // OR
    // (className | varName) '.' subroutineName '(' expressionList ')'
    if (have("symbol", "(")) {
        subroutineCall->addChild(mustBe("symbol", "("));
        subroutineCall->addChild(compileExpressionList());
        subroutineCall->addChild(mustBe("symbol", ")"));
    } else if (have("symbol", ".")) {
        subroutineCall->addChild(mustBe("symbol", "."));
        subroutineCall->addChild(mustBe("identifier", ""));  // Expect subroutineName
        subroutineCall->addChild(mustBe("symbol", "("));
        subroutineCall->addChild(compileExpressionList());
        subroutineCall->addChild(mustBe("symbol", ")"));
    } else {
        throw ParseException();
    }

    return subroutineCall;
}