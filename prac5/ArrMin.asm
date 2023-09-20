// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@R1
D=M-1
@R2
M=M+D

@32767
D=A
@R0
M=D

(LOOP)
(TERMINATION)
	@R1
	D=M
	@R2
	D=D-M
	@END
	D;JGT
	@R1
	A=M
	D=M
    @CHECK_P
    D;JGE // if statement if D >= 0
	@CHECK_N
	0;JMP // this is like an else statement
(UPDATE)
	@R1
	A=M
	D=M
	@R0
	M=D
(CONTINUE)
	@R1
	M=M+1
	@LOOP
	0;JMP
(END)
	@END
	0;JMP

(OUT_N)
    @R1
	A=M
	D=M
	@R0
	D=D-M 
    @CONTINUE
	D;JGE
    @UPDATE
    0;JMP
    
(OUT_P)
    @R1
	A=M
	D=M
	@R0
	D=D-M 
    @CONTINUE
	D;JGE
    @UPDATE
    0;JMP

(CHECK_N)
    @R0
    D=M
    @OUT_N
    D;JLT
    @UPDATE
    0; JMP

(CHECK_P)
    @R0
    D=M
    @OUT_P
    D;JGE
    @CONTINUE
    0;JMP