// Sorts the array of length R2 whose first element is at RAM[R1] in ascending order in place. Sets R0 to True (-1) when complete.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// Increment R2 by R1 - 1 to get the ending address of the array.
@R1
D=M-1
@R2
M=M+D

// First loop (LOOP1) to iterate through the array.
(LOOP1)
(TERMINATION)
    // Load the values in R1 and R2, and compare them.
    @R1
    D=M
    @R2
    D=D-M
    // If R1 > R2, end the loop.
    @LOOP1_END
    D;JGT
    // Increment R1 to move to the next element.
    @R1
    D=M
    @R3
    M=D+1

// Second loop (LOOP2) to perform the sorting.
(LOOP2)
(TERMINATION2)
    // Load the values in R3 and R2, and compare them.
    @R3
    D=M
    @R2
    D=D-M
    // If R3 > R2, end the loop.
    @LOOP2_END
    D;JGT
    // Load the value at R3 into D and compare it to the value at R1.
    @R3
    A=M
    D=M
    @CHECK_P
    D;JGE
    @CHECK_N
    0;JMP


// Output for negative values.
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


// Swap values if necessary.
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

// End of the second loop (LOOP2).
(LOOP2_END)
    @R1
    M=M+1
    @LOOP1
    0;JMP

// End of the first loop (LOOP1).
(LOOP1_END)
    @R0
    M=-1
    @END
    0;JMP

// Continue the loop.
(CONTINUE)
    @R3
    M=M+1
    @LOOP2
    0;JMP


// Check for positive values.
(CHECK_P)
    @R1
    A=M
    D=M
    @OUT_P
    D;JGE
    @CONTINUE
    0;JMP


// Check for negative values.
(CHECK_N)
    @R1
    A=M
    D=M
    @OUT_N
    D;JLT
    @SWITCH
    0;JMP


// Output for positive values.
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


