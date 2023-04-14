ARITH_UNARY = {
    'neg': "@SP\n A=M-1\n M=M\n",
    'not': "@SP\n A=M-1\n M=!M\n"
}


ARITH_BINARY = {
    'add': "@SP\n A=M-1\n D=D+M\n M=D\n",
    'sub': "@SP\n A=M-1\n D=D-M\n M=D\n",
    'and': "@SP\n A=M-1\n D=D&M\n M=D\n",
    'or': "@SP\n A=M-1\n D=D|M\n M=D\n"
}

def getPushD():
    return "@SP\nA=M\nM=D\n@SP\nM=M+1\n"

def getPopD():
    return "@SP\nM=M-1\nA=M\nD=M\n"

def pointerSeg(push,seg,index):
    # The following puts the segment's pointer + index in the D
    # register, then achives its aim of either pushing RAM[seg+index]
    # to the stack or poping the stack to RAM[seg+index]. This will
    # work for ARG, LCL, THIS, and THAT segements
    # 
    # INPUTS:
    # push - a string that defines 'push' or 'pop' the operation occuring
    # seg - a string that specifies the segment being worked with, 
    # here it is LCL, ARG, THIS, or THAT
    # index - an integer that species the offset from the segment's base address
    # OUTPUTS:
    # a string of hack machine language instructions that performs push/pop seg index
    assemb = ''
    indexString = str(index)
    getLCL = "@" + seg + "\nD=M\n@" + indexString +"\nD=D+A"
    assemb += getLCL

    if (push == 'push'):
        assemb += 
    elif (push == 'pop'):
        assemb += 


    return assemb

def constantSeg(push,seg,index):
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
    assemb = ''


    return assemb



def fixedSeg(push,seg,index):
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
    assemb = ''


    return assemb



def getGoto(label):
    #if we see a goto jump to execute command just after label
    return @label, 0;JMP, 

def getLabel(label):
    return "(" + label + ")"

def getIfgoto(label):
    assemb = ''
    assemb += getPopD()        # Pop the value at the top of the stack into the D register
    assemb += "@" + label + "\n"  # Load the label's address into the A register
    assemb += "D;JNE\n"       # Jump to the label if the value in D is not zero
    return assemb
