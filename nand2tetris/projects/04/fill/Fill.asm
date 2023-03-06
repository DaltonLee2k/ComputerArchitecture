// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infLOOPe loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


(LOOP)
	//set screen counter to screen address (16384)
	@SCREEN
	D=A
	@SCREEN_COUNTER
	M=D

			//Set screen end to the value of the final pixel in the scren 
	@24575 //# of pixels in screen
	D=A
	@SCREEN_END
	M=D


	@KBD
	D=M
	@WHITE
	D;JEQ

	@color
	M=-1 // color set to black

	@FILL
	0;JMP

(WHITE)
	@color //just switches the color 
	M=0
    @FILL
    0;JMP

(FILL)
	//While counts <= end set M of screen counter to color
	@SCREEN_COUNTER
	D=M
	@SCREEN_END
	D=D-M
	@LOOP
	D;JEQ

	// change the memory pointed at by the screen pointer
	@color
	D=M
	@SCREEN_COUNTER
	A=M
	M=D

	//iterate screen counter
	@SCREEN_COUNTER
	M=M+1

	@FILL
	0;JMP