// This file is based on part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: Mult.asm

// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
// @R0
// M = 0
// @R1
// D = M
// @STEP
// D; JGT

// @END
// 0; JMP

// (STEP)
// @R0
// D = M
// @R2
// D = D + M
// @R0
// M = D
// @R1
// D = M - 1
// M = D
// @STEP
// D; JGT

// (END)
// @END
// 0; JMP
@sgn
M=0
(R1_SGN)
@R1
D=M
@R1_A
D;JLT
(CHECK_R2)
@R2
D=M
@R2_A
D;JLT

(ENTRY)
@R1
D=M
@R2
D=D-M
@CHANGE
D;JLT

(LOOP)
@R2
MD=M-1
@CHECK_sgn
D;JLT
@R1
D=M
@R0
M=M+D
@LOOP
0;JMP

(CHECK_sgn)
@sgn
D=M
@END
D;JEQ
@R0
M=-M
@END
0;JMP

(END)
@END
0;JMP

(R2_A)
@sgn
M=!M
@R2
M=-M
@ENTRY
0;JMP

(R1_A)
@sgn
M=!M
@R1
M=-M
@CHECK_R2
0;JMP

(CHANGE)
@R1
D=M
@temp
M=D
@R2
D=M
@R1
M=D
@temp
D=M
@R2
M=D
@LOOP
0;JMP

