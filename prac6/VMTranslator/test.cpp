string VMTranslator::vm_push(string segment, int offset){
    string translator="";
    if (segment=="constant") {
        translator=translator+"@"+to_string(offset) +"\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"; 
    } else if (segment =="static") {
        translator=translator+"@"+to_string(offset+16)+"\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n";
    } else {
        translator=translator+"@"+to_string(offset)+"\nD=A\n"; 
        if (segment=="this") {
            translator=translator+"@THIS\nA=M+D\n";
        } else if (segment=="that") {
            translator=translator+"@THAT\nA=M+D\n";
        } else if (segment=="temp") {
            translator=translator+"@R5\nA=A+D\n";
        } else if (segment=="local") {
            translator=translator+"@LCL\nA=M+D\n";
        } else if (segment=="argument") {
            translator=translator+"@ARG\nA=M+D\n";
        } else if (segment=="pointer") {
            translator=translator+"@R3\nA=A+D\n";
        }
        translator=translator+"D=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n";
    }
    return translator;
}

/** Generate Hack Assembly code for a VM pop operation */
string VMTranslator::vm_pop(string segment, int offset) {
    string translator = "";
    if (segment == "static") {
        translator = "@SP\nAM=M-1\nD=M\n@" + to_string(offset + 16) + "\nM=D\n";
    } else {
        translator = "@" + to_string(offset) + "\nD=A\n";
        if (segment == "this") {
            translator += "@THIS\nD=M+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n";
        } else if (segment == "that") {
            translator += "@THAT\nD=M+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n";
        } else if (segment == "temp") {
            translator += "@R5\nD=A+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n";
        } else if (segment == "local") {
            translator += "@LCL\nD=M+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n";
        } else if (segment == "argument") {
            translator += "@ARG\nD=M+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n";
        } else if (segment == "pointer") {
            translator += "@R3\nD=A+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n";
        }
    }
    return translator;
}