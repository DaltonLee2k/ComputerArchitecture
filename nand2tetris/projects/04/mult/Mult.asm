// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.




@R2
M=0    //set product = 0
@i     // set i = 0 
M=0     

(LOOP)

@i
D=M     //set d to i value
@R0     
D=D-M   
@STOP
D;JGE    //Stop if we have looped R0 times

@R1
D=M     //set D to R1 so it can be added to R2
@R2     
M=D+M   //Add R1 value to product

@i
M=M+1   //iterate i
@LOOP   //go back to loop
0;JMP

(STOP)
@STOP
0;JMP //weird infinite loop
