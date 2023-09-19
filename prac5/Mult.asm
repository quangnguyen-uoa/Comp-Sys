// This file is based on part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: Mult.asm

// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
@R0
M = 0
@R1
D = M
@STEP
D; JGT

@END
0; JMP

(STEP)
@R0
D = M
@R2
D = D + M
@R0
M = D
@R1
D = M - 1
M = D
@STEP
D; JGT

(END)
@END
0; JMP

