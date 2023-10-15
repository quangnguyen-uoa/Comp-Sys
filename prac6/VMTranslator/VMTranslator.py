class VMTranslator:

    def vm_push(segment, offset):
        '''Generate Hack Assembly code for a VM push operation'''
        if(segment == "constant"):
            code = f"@{offset}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif(segment == "local"):
            code = f"@{offset}\nD=A\n@LCL\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif (segment == "argument"):
            code = f"@{offset}\nD=A\n@ARG\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif (segment == "this"):
            code = f"@{offset}\nD=A\n@THIS\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif (segment == "that"):
            code = f"@{offset}\nD=A\n@THAT\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif (segment == "temp"):
            code = f"@{offset}\nD=A\n@5\nA=A+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif (segment == "pointer"):
            if offset == '0':
                offset = 'THIS'
            else:
                offset = 'THAT'
            code = f"@{offset}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif (segment == "static"):
            code = f"@{offset}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        
        return code

    def vm_pop(segment, offset):
        '''Generate Hack Assembly code for a VM pop operation'''
        if (segment == "local"):
            code = f"@{offset}\nD=A\n@LCL\nD=M+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif (segment == "argument"):
            code = f"@{offset}\nD=A\n@ARG\nD=M+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif (segment == "this"):
            code = f"@{offset}\nD=A\n@THIS\nD=M+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif (segment == "that"):
            code = f"@{offset}\nD=A\n@THAT\nD=M+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif (segment == "temp"):
            code = f"@{offset}\nD=A\n@5\nD=A+D\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif (segment == "pointer"):
            if offset == '0':
                offset = 'THIS'
            else:
                offset = 'THAT'   
            code = f"@SP\nAM=M-1\nD=M\n@{offset}\nM=D\n"
        elif (segment == "static"):
            code = f"@SP\nAM=M-1\nD=M\n@{offset}\nM=D\n"
            
        return code

    def vm_add():
        '''Generate Hack Assembly code for a VM add operation'''
        return "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=D+M\n"

    def vm_sub():
        '''Generate Hack Assembly code for a VM sub operation'''
        return "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=M-D\n"

    def vm_neg():
        '''Generate Hack Assembly code for a VM neg operation'''
        return "@SP\nA=M-1\nM=-M\n"

    def vm_eq():
        '''Generate Hack Assembly code for a VM eq operation'''
        return "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@EQUAL_T\nD;JEQ\n@SP\nA=M-1\nM=0\n@EQ_TERMINATE\n0;JMP\n(EQUAL_T)\n@SP\nA=M-1\nM=-1\n(EQ_TERMINATE)\n"

    def vm_gt():
        '''Generate Hack Assembly code for a VM gt operation'''
        return "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@GREAT_T\nD;JGT\n@SP\nA=M-1\nM=0\n@GREAT_TERMINATE\n0;JMP\n(GREAT_T)\n@SP\nA=M-1\nM=-1\n(GREAT_TERMINATE)\n"

    def vm_lt():
        '''Generate Hack Assembly code for a VM lt operation'''
        return "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nD=M-D\n@LESS_T\nD;JLT\n@SP\nA=M-1\nM=0\n@LESS_TERMINATE\n0;JMP\n(LESS_T)\n@SP\nA=M-1\nM=-1\n(LESS_TERMINATE)\n"

    def vm_and():
        '''Generate Hack Assembly code for a VM and operation'''
        return "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=D&M\n"

    def vm_or():
        '''Generate Hack Assembly code for a VM or operation'''
        return "@SP\nM=M-1\nA=M\nD=M\nA=A-1\nM=D|M\n"

    def vm_not():
        '''Generate Hack Assembly code for a VM not operation'''
        return "@SP\nA=M-1\nM=!M\n"

    def vm_label(label):
        '''Generate Hack Assembly code for a VM label operation'''
        return f"({label})\n"

    def vm_goto(label):
        '''Generate Hack Assembly code for a VM goto operation'''
        return f"@{label}\n" + "0;JMP\n"

    def vm_if(label):
        '''Generate Hack Assembly code for a VM if-goto operation'''
        return "@SP\n" + "AM=M-1\n" + "D=M\n" + f"@{label}\n" + "D;JNE\n"

    def vm_function(function_name, n_vars):
        '''Generate Hack Assembly code for a VM function operation'''
        return ""

    def vm_call(function_name, n_args):
        '''Generate Hack Assembly code for a VM call operation'''
        return ""

    def vm_return():
        '''Generate Hack Assembly code for a VM return operation'''
        return ""

# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if(len(tokens)==1):
                    if(tokens[0]=='add'):
                        print(VMTranslator.vm_add())
                    elif(tokens[0]=='sub'):
                        print(VMTranslator.vm_sub())
                    elif(tokens[0]=='neg'):
                        print(VMTranslator.vm_neg())
                    elif(tokens[0]=='eq'):
                        print(VMTranslator.vm_eq())
                    elif(tokens[0]=='gt'):
                        print(VMTranslator.vm_gt())
                    elif(tokens[0]=='lt'):
                        print(VMTranslator.vm_lt())
                    elif(tokens[0]=='and'):
                        print(VMTranslator.vm_and())
                    elif(tokens[0]=='or'):
                        print(VMTranslator.vm_or())
                    elif(tokens[0]=='not'):
                        print(VMTranslator.vm_not())
                    elif(tokens[0]=='return'):
                        print(VMTranslator.vm_return())
                elif(len(tokens)==2):
                    if(tokens[0]=='label'):
                        print(VMTranslator.vm_label(tokens[1]))
                    elif(tokens[0]=='goto'):
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif(tokens[0]=='if-goto'):
                        print(VMTranslator.vm_if(tokens[1]))
                elif(len(tokens)==3):
                    if(tokens[0]=='push'):
                        print(VMTranslator.vm_push(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='pop'):
                        print(VMTranslator.vm_pop(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='function'):
                        print(VMTranslator.vm_function(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='call'):
                        print(VMTranslator.vm_call(tokens[1],int(tokens[2])))

        