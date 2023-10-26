#ifndef COMPILERPARSER_H
#define COMPILERPARSER_H

#include <list>
#include <exception>

#include "ParseTree.h"
#include "Token.h"

using namespace std;

class CompilerParser {
    public:
        CompilerParser(list<Token*> tokens);

        ParseTree* compileProgram();
        ParseTree* compileClass();
        ParseTree* compileClassVarDec();
        ParseTree* compileSubroutine();
        ParseTree* compileParameterList();
        ParseTree* compileSubroutineBody();
        ParseTree* compileVarDec();

        ParseTree* compileStatements();
        ParseTree* compileLet();
        ParseTree* compileIf();
        ParseTree* compileWhile();
        ParseTree* compileDo();
        ParseTree* compileReturn();

        ParseTree* compileExpression();
        ParseTree* compileTerm();
        ParseTree* compileExpressionList();
        
        void next();
        Token* current();
        bool have(string expectedType, string expectedValue);
        Token* mustBe(string expectedType, string expectedValue);
    private:
        list<Token*> toks;
        list<Token*>::iterator pos;
        //helper methods
        ParseTree* compileSubroutineCall();
        bool isOperator (const string& symbol); 
        bool haveNext();
};

class ParseException : public exception {
    public:
        const char* what();
};

#endif /*COMPILERPARSER_H*/