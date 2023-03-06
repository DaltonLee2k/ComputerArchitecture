#Necessary Functions

def dest2bin(mnemonic):
    # returns the binary code for the destination part of a C-instruction


    destBin = 0
    return destBin

def comp2bin(mnemonic):
    # returns the binary code for the comp part of a C-instruction
    
    compBin = 0
    return compBin

def jump2bin(mnemonic):
    # returns the binary code for the jump part of a C-instruction
    
    jumpBin = 0
    return jumpBin
    
def commandType(command):
    # returns "A_COMMAND", "C_COMMAND", or "L_COMMAND"
    # depending on the contents of the 'command' string
    pass

def getSymbol(command):
    # given an A_COMMAND or L_COMMAND type, returns the symbol as a string,
    # eg (XXX) returns 'XXX'
    # @sum returns 'sum'
    pass

def getDest(command):
    # return the dest mnemonic in the C-instruction 'commmand'
    pass

def getComp(command):
    # return the comp mnemonic in the C-instruction 'commmand'
    pass

def getJump(command):
    # return the jump mnemonic in the C-instruction 'commmand'
    pass
    