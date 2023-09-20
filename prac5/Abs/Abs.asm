// Calculates the absolute value of R1 and stores the result in R0.
// (R0, R1 refer to RAM[0], and RAM[1], respectively.)

// Put your code here.
@R1
D = M
@NEG
D; JLT

@R0
M = D
@END
0; JMP

(NEG)
D = -D
@R0
M = D

(END)