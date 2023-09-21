// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// Initialize R2 to (R1 - 1).
@R1
D=M-1
@R2
M=M+D

// Set R0 to 32767 (0x7FFF).
@32767
D=A
@R0
M=D

// Loop (LOOP) to iterate through the array.
(LOOP)
(TERMINATION)
	// Load the values in R1 and R2, and compare them.
	@R1
	D=M
	@R2
	D=D-M
	@END
	D;JGT       // If R1 > R2, end the loop.
	@R1
	A=M
	D=M
    @CHECK_P
    D;JGE      // If D >= 0, jump to CHECK_P
	@CHECK_N
	0;JMP      // Otherwise, jump to CHECK_N

// Update R0 with the value in memory.
(UPDATE)
	@R1
	A=M
	D=M
	@R0
	M=D

// Continue the loop.
(CONTINUE)
	@R1
	M=M+1
	@LOOP
	0;JMP

// End of the loop (LOOP).
(END)
	@END
	0;JMP

// Output for negative values (OUT_N).
(OUT_N)
    @R1
	A=M
	D=M
	@R0
	D=D-M 
    @CONTINUE
	D;JGE      // If D >= 0, jump to UPDATE
    @UPDATE
    0;JMP

// Output for positive values (OUT_P).
(OUT_P)
    @R1
	A=M
	D=M
	@R0
	D=D-M 
    @CONTINUE
	D;JGE      // If D >= 0, jump to UPDATE
    @UPDATE
    0;JMP

// Check for negative values (CHECK_N).
(CHECK_N)
    @R0
    D=M
    @OUT_N
    D;JLT      // If D < 0, jump to OUT_N
    @UPDATE
    0; JMP

// Check for positive values (CHECK_P).
(CHECK_P)
    @R0
    D=M
    @OUT_P
    D;JGE      // If D >= 0, jump to OUT_P
    @CONTINUE
    0;JMP