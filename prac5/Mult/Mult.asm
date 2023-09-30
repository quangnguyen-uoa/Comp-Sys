// This file is based on part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: Mult.asm

// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@sgn
M=0            // Initialize sgn (sign) flag to 0


(R2_SGN)
@R2
D=M            // Load the value in R2 into D
@R2_A
D; JLT          // If it's negative (less than 0), jump to BEGIN

(R1_SGN)
@R1
D=M            // Load the value in R1 into D
@R1_A
D; JLT          // If it's negative (less than 0), jump to R2_SGN



(BEGIN)
@R1
D=M            // Load the value in R1 into D
@R2
D=D-M          // Subtract the value in R2 from D
@CHANGE
D;JLT          // If D is negative, jump to CHANGE

(LOOP)
@R2
MD=M-1         // Decrement the value in R2
@CHECK_sgn
D;JLT          // If R2 is less than 0, jump to CHECK_sgn
@R1
D=M            // Load the value in R1 into D
@R0
M=M+D          // Add D to the value in R0
@LOOP
0;JMP          // Repeat the LOOP

(END)
@END
0;JMP          // Infinite loop (program ends)

(CHECK_sgn)
@sgn
D=M            // Load the sgn flag into D
@END
D;JEQ          // If sgn is 0, jump to END
@R0
M=-M          // Negate the value in R0
@END
0;JMP          // Jump to END


(CHANGE)
@R1
D=M            // Load the value in R1 into D
@temp
M=D            // Store D in a temporary location
@R2
D=M            // Load the value in R2 into D
@R1
M=D            // Copy D into R1
@temp
D=M            // Retrieve the value from the temporary location
@R2
M=D            // Copy D into R2
@LOOP
0; JMP          // Jump to LOOP

(R1_A)
@sgn
M=!M           // Invert the sgn flag
@R1
M=-M           // Negate the value in R1
@R2_SGN
0; JMP          // Jump to R2_SGN


(R2_A)
@sgn
M=!M           // Invert the sgn flag
@R2
M=-M           // Negate the value in R2
@BEGIN
0; JMP          // Jump to BEGIN