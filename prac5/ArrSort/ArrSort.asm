// Sorts the array of length R2 whose first element is at RAM[R1] in ascending order in place. Sets R0 to True (-1) when complete.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R1 
D=M-1 
@R2 
M=M+D 

(LOOP1)
(TERMINATION)
    @R1
    D=M
    @R2
    D=D-M
    @LOOP1_END
    D;JGT
    @R1
    D=M
    @R3 
    M=D+1 


(LOOP2)
(TERMINATION2)
    @R3
    D=M
    @R2
    D=D-M
    @LOOP2_END
    D;JGT
    @R3 
    A=M
    D=M 
    @CHECK_P
    D;JGE
    @CHECK_N
    0;JMP
(SWITCH)
    @R1
    A=M
    D=M
    @temp
    M=D
    @R3
    A=M
    D=M
    @R1
    A=M
    M=D
    @temp
    D=M
    @R3
    A=M
    M=D
(CONTINUE)
    @R3
    M=M+1
    @LOOP2
    0;JMP

(LOOP2_END)
    @R1
    M=M+1
    @LOOP1
    0;JMP

(LOOP1_END)
    @R0
    M=-1
(END)
    @END
    0;JMP

(OUT_N)
    @R3
    A=M
    D=M
    @R1
    A=M
    D=D-M 
    @CONTINUE
    D;JGE
    @SWITCH
    0;JMP

(OUT_P)
    @R3
    A=M
    D=M
    @R1
    A=M
    D=D-M 
    @CONTINUE
    D;JGE
    @SWITCH
    0;JMP

(CHECK_N)
    @R1
    A=M
    D=M
    @OUT_N
    D;JLT
    @SWITCH
    0;JMP

(CHECK_P)
    @R1
    A=M
    D=M
    @OUT_P
    D;JGE
    @CONTINUE
    0;JMP
