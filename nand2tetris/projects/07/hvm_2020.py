#!/usr/bin/python3
import os
import sys

# The following are declared at the top of the file to make them accessible with the functions that follow.

# Note the code segments in ARITH_BINARY dictionary are to be prefaced with a popD() command.
ARITH_BINARY = {
    "add": "A=A-1, M=M+D,",
    "sub": "A=A-1, M=M-D,",
    "and": "A=A-1, M=M&D,",
    "or": "A=A-1, M=M|D,",
}

# ARITH_UNARY returns the asm code required to negate and not the top value in the stack
ARITH_UNARY = {"neg": "@SP, A=M-1, M=-M,", "not": "@SP, A=M-1, M=!M,"}

# ARITH_TEST and SEGLABEL are simple translation dictionaries.
ARITH_TEST = {"gt": "JGT", "lt": "JLT", "eq": "JEQ"}

# Converts from vm language to asm representation.
SEGLABEL = {"argument": "ARG", "local": "LCL", "this": "THIS", "that": "THAT"}


# For creating unique labels.
LABEL_NUMBER = 0


def pointerSeg(push, seg, index):
    # The following puts the segment's pointer + index in the D
    # register, then achives its aim of either pushing RAM[seg+index]
    # to the stack or poping the stack to RAM[seg+index]. This will
    # work for ARG, LCL, THIS, and THAT segements
    # INPUTS:
    # push - a string that defines 'push' or 'pop' the operation occuring
    # seg - a string that specifies the segment being worked with,
    # here it is LCL, ARG, THIS, or THAT
    # index - an integer that species the offset from the segment's base address
    # OUTPUTS:
    # a string of hack machine language instructions that performs push/pop seg index
    instr = "@%s, D=M, @%d, D=D+A," % (SEGLABEL[seg], int(index))
    if push == "push":
        return instr + ("A=D, D=M," + getPushD())
    elif push == "pop":
        return instr + "@R15, M=D," + getPopD() + "@R15, A=M, M=D,"
    else:
        print("Yikes, pointer segment, bet seg not found.")


def fixedSeg(push, seg, index):
    # The following puts the segment's value + index in the D
    # register and then either pops from the stack to that address
    # or pushes from that address to the stack. Note that for fixed segments
    # the base address is 'fixed' as follows and is NOT a pointer:
    # pointer = 3
    # temp    = 5
    # INPUTS:
    # push - a string that defines 'push' or 'pop' the operation occuring
    # seg - a string that specifies the segment being worked with,
    # here 'pointer' or 'temp'
    # index - an integer that species the offset from the segment's base address
    # OUTPUTS:
    # a string of hack machine language instructions that performs push/pop seg index
    if push == "push":
        if seg == "pointer":
            return "@%d, D=M," % (3 + int(index)) + getPushD()
        elif seg == "temp":
            return "@%d, D=M," % (5 + int(index)) + getPushD()
    elif push == "pop":
        if seg == "pointer":
            return getPopD() + "@%d, M=D," % (3 + int(index))
        elif seg == "temp":
            return getPopD() + "@%d, M=D," % (5 + int(index))
    else:
        print("Yikes, fixed segment, bet seg not found.")


def constantSeg(push, seg, index):
    # This function returns a sequence of machine language
    # instructions that places a constant value onto the
    # top of the stack. Note pop is undefined for this
    # function if seg is 'constant'. However, this function
    # also addresses seg = 'static', for which pop is defined.
    # NOTE: For seg = 'static' the filename is needed. This can be a global
    # or you can change the parameters to the function.

    # INPUTS:
    # push - a string that defines 'push' or 'pop' the operation occuring
    # seg - a string that specifies the segment being worked with, here 'constant' or 'static'
    # index - an integer that species the offset in general, but here is the literal value
    # OUTPUTS:
    # a string of hack machine language instructions that perform push/pop seg index
    # if push = 'push', seg = 'constant', and index = an integer
    # or if push = 'push' or 'pop', seg = 'static' and index = and integer
    global filename
    fn_ = filename.split("/")
    fn_ = fn_[-1]
    fn_ = fn_.split(".")
    fn_ = fn_[0]
    if seg == "constant":
        return "@%d,    D=A," % (int(index)) + getPushD()
    elif seg == "static" and push == "push":
        return "@%s.%d, D=M," % (fn_, int(index)) + getPushD()
    elif seg == "static" and push == "pop":
        return getPopD() + "@%s.%d, M=D," % (fn_, int(index))


# SEGMENTS maps the vm command to a function handle that generates the code for the command
# Withholding parentheses makes it like an entire function is the value for each key, allowing clients to pass arguments to keys.
SEGMENTS = {
    "constant": constantSeg,
    "static": constantSeg,
    "pointer": fixedSeg,
    "temp": fixedSeg,
    "local": pointerSeg,
    "argument": pointerSeg,
    "this": pointerSeg,
    "that": pointerSeg,
}


def line2Command(l):
    # This function just strips commands that follow comments.
    return l[: l.find("//")].strip()


def uniqueLabel():
    # Returns a unique label.
    # Access global variable defined at the top of file, increment and return a unique label: UL_LABEL_NUMBER where label number is an integer.
    global LABEL_NUMBER
    LABEL_NUMBER += 1
    return "UL_" + str(LABEL_NUMBER)


def getPushD():
    # This method takes no arguments and returns a string with assembly language
    # that will push the contents of the D register to the stack.
    return "@SP, A=M, M=D, @SP, M=M+1,"


def getPopD():
    # This method takes no arguments and returns a string with assembly language
    # that will pop the stack to the D register.
    # SIDE EFFECT: The A register contains the SP.
    return "@SP, AM=M-1, D=M,"


def ParseFile(f):
    # Main parsing loop, takes a file handle, returns a string representation of
    # the assembly code corresponding to the .vm
    outString = ""
    for line in f:
        command = line2Command(line)  # strip any comments
        # Process the line if characters still exist after removing comments
        if command:
            # Split and strip the line into separated tokens stored in list args[].
            args = [x.strip() for x in command.split()]
            # Process a binary operation (add, sub, and, or)
            if args[0] in ARITH_BINARY.keys():
                # Prepare to use the ARITH_BINARY dict by placing y in d-register and THEN processing the correct operation (remember ARITH_BINARY assumption of popD).
                outString += getPopD()
                outString += ARITH_BINARY[args[0]]
            # Process a unary operation (neg, not)
            # note: ARITH_UNARY dict processes stack values in-place.
            elif args[0] in ARITH_UNARY.keys():
                outString += ARITH_UNARY[args[0]]
            # Process comparison operation (lt, gt, eq)
            elif args[0] in ARITH_TEST.keys():
                # HACK ALERT - this shoul be a function, but I got lazy.
                outString += getPopD()
                # Use sub method to determine d-register value.
                outString += ARITH_BINARY["sub"]
                outString += getPopD()
                # Return unique label via function so that multiple comparisons can occur in a single program by giving each unique labels.
                l1 = uniqueLabel()
                l2 = uniqueLabel()
                # Create the asm code that carries out the comparison operation using unique labels generated above and a dictionary translation from ARITH_TEST.
                js = "@%s, D;%s, @%s, D=0;JMP, (%s),D=-1,(%s)," % (
                    l1,
                    ARITH_TEST[args[0]],
                    l2,
                    l1,
                    l2,
                )
                outString += js
                outString += getPushD()
            # Any valid vm code that makes it to this elif statement will be a call to push/pop using specified segments of memory.
            elif args[1] in SEGMENTS.keys():
                # ALERT - this is a nice way of calling functions in a dictionary.
                # Study this line closely.
                # Actual function is stored as value for specified key rather than a function call. This allows clients to pass arguments to the value of a dict.
                outString += SEGMENTS[args[1]](args[0], args[1], args[2])
            # Account for invalid vm code and stop the program upon encountering. Any line that reaches this else statement is NOT valid vm code.
            else:
                print("Unknown command!")
                print(args)
                # non-zero argument in sys.exit() indicates abnormal exit (error)
                sys.exit(-1)
    # Use another unique label to ensure program termination using an infinite loop as prompted.
    l = uniqueLabel()
    outString += "(%s)" % (l) + ",@%s,0;JMP" % l  # Final endless loop

    # replace commas with newlines before returning
    return outString.replace(" ", "").replace(",", "\n")


# Strip the filename to include no whitespace.
filename = sys.argv[1].strip()

# This is ugly - add some error checking on file open.
f = open(filename)
# Just print to command line. To output to a file use unix/windows redirection
# from the command line, for example
# >>python hvm_2020.py simpleAdd.vm > simpleAdd.asm
print(ParseFile(f))
f.close()


def getGoto(label):
    #if we see a goto jump to execute command just after label
    return "@"+label+"\n 0;JMP" 

def getLabel(label):
    return "(" + label + ")\n"

def getIfgoto(label):
    assemb = ''
    assemb += getPopD()        # Pop the value at the top of the stack into the D register
    assemb += "@" + label + "\n"  # Load the label's address into the A register
    assemb += "D;JNE\n"       # Jump to the label if the value in D is not zero
    return assemb


def _getPushMem(src):
    #take whats in local and push it to the stack
    # INPUT: src - a text string that is a symbol corresponding to a RAM address containing an address
    # OUTPUT: a text string that will result in the address in src being pushed 
    # to the top of the stackM. 
    assemb = '@'+src+'\n'+'D=\n'
    assemb += getPushD


    return assemb

    

def _getPushLabel(src):
    # INPUT: src - a text string that is some label, eg '(MAIN_LOOP)' which 
    # corresponds to a ROM address in the symbol table.
    # OUTPUT: a text string that will result in the ROM address 
    # to the top of the stack.
    assemb = '@'+src+'\n'+'D=A\n'
    assemb += getPushD


    return assemb

def _getPopMem(dest):
    # something from teh stack to specific location
    # INPUT: src - a text string that is a symbol that corresponding to a RAM address containing an address
    # OUTPUT: a text string that pops the stack and places that value into the dest segment pointer
    assemb = getPopD
    assemb += "@"+dest+"\nM=D\n"

    return assemb 

def _getMoveMem(src,dest):
    #Move somethings thats in one space into another
    # INPUT: src - a text string that is a symbol corresponding to a RAM address containing an address
    # INPUT: dest- a text string that is a symbol corresponding to a RAM address containing an address
    # OUPUT: a text string that copies the address in src to dest
    assemb = '''
        @{0}
        D=M
        @{1}
        M=D
    '''.format(src, dest)

    return assemb 


def getCall(functionName, nargs):
    """
    Generate assembly code for a function call.

    INPUT:
    - functionName: name of the function to call
    - nargs: number of arguments to pass

    OUTPUT:
    - Assembly code for the function call
    """
    # push return address
    return_address = functionName + uniqueLabel() 
    assemb = "@{}\nD=A\n".format(return_address)
    assemb += getPushD
    # push LCL
    assemb += _getPushMem("LCL")
    # push ARG
    assemb += _getPushMem("ARG")
    # push THIS
    assemb += _getPushMem("THIS")
    # push THAT
    assemb += _getPushMem("THAT")
    # ARG = SP - nargs - 5
    assemb += "@SP\nD=M\n"
    assemb += "@{}\nD=D-A\n".format(nargs+5)
    assemb += "@ARG\nM=D\n"
    # LCL = SP
    assemb += "@SP\nD=M\n@LCL\nM=D\n"
    # jump to function
    assemb += "@{}\n0;JMP\n".format(functionName)
    # define return address label
    assemb += "({})\n".format(getLabel(return_address))
    return assemb


def getFunction(functionName,nLocals):
    # Store functionName in label format (i.e. functionName$labelIndex)
    # Declare the label
    assemb = getLabel(functionName)
    
    # Repeat nLocals times
    for i in range(nLocals):
        # Initialize local variable to 0
        assemb += "@0\nD=A\n"
        assemb += getPushD()
    return assemb


def getReturn():
    # Save endFrame = LCL, then set R13 = endFrame
    assemb = "@LCL\nD=M\n@R13\nM=D\n"

    # Save retAddr = *(endFrame - 5), then set ARG = retAddr + 1
    assemb += "@5\nD=A\n@R13\nA=M-D\nD=M\n@R14\nM=D\n"
    assemb += "@ARG\nD=M\n@R15\nM=D+1\n"

    # Restore segment pointers of the caller
    segment_pointers = [("THAT", 1), ("THIS", 2), ("ARG", 3), ("LCL", 4)]
    for segment, offset in segment_pointers[::-1]:
        assemb += f"@R13\nAM=M-1\nD=M\n@{segment}\nM=D\n"

    # Jump to retAddr
    assemb += "@R14\nA=M\n0;JMP\n"

    return assemb
    pass


def getInit(sysinit = True):
    """

    Write the VM initialization code:
        Set the SP to 256.
        Initialize system pointers to -1.
        Call Sys.Init()
        Halt loop
    Passing sysinit = False oly sets the SP.  This allows the simpler
    VM test scripts to run correctly.
    """
    os = ""
    os += '@256,D=A,@SP,M=D,'
    if sysinit:
        os += 'A=A+1,M=-1,A=A+1,M=-1,A=A+1,M=-1,A=A+1,M=-1,'  # initialize ARG, LCL, THIS, THAT
        os += getCall('Sys.init', 0) # release control to init
        halt = uniqueLabel()
        os += '@%s, (%s), 0;JMP,' % (halt, halt)
    return os