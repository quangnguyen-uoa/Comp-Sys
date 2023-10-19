asm = [
            # push return address
            "@{fn_nam}$ret.{fn_return_idx}",
            "D=A", 
            "@SP", 
            "A=M",
            "M=D",
            "@SP", 
            "M=M+1",
            # push lcl into stack
            "@LCL", 
            "D=M",
            "@SP", 
            "A=M",
            "M=D",
            "@SP", 
            "M=M+1",
            # push arg into stack
            "@ARG", 
            "D=M",
            "@SP", 
            "A=M",
            "M=D",
            "@SP", 
            "M=M+1",
            # push this into stack
            "@THIS", 
            "D=M",
            "@SP", 
            "A=M",
            "M=D",
            "@SP", 
            "M=M+1",
            # push that into stack
            "@THAT", 
            "D=M",
            "@SP", 
            "A=M",
            "M=D",
            "@SP", 
            "M=M+1",
            # compute (SP - 5 - nargs) so we can reposition our argument pointer
            "@5",
            "D=A",
            "@SP",
            "D=M-D",
            "@{arg_count}",
            "D=D-A",
            # reposition arg which sets the pointer to the first argument we pushed for this function call
            "@ARG",
            "M=D",
            # LCL = SP. Basically, our local segment starts right after the call frame we created (through pushing)
            "@SP",
            "D=M",
            "@LCL",
            "M=D",
            # jump to our function and let the magic happen
            "@{fn_name}",
            "0;JMP",
            # set return label. This is where we want the function to continue from
            "({fn_name}$ret.{fn_return_idx})"
        ]

assembly_code_string = "\n".join(asm)
print(assembly_code_string)