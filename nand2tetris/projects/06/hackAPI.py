#Necessary Functions

def dest2bin(mnemonic):
    # returns the binary code for the destination part of a C-instruction
    destTable = {
        "null": "000",
        "M": "001", 
        "D": "010",
        "DM": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "ADM": "111"
    }

    destBin = destTable.get(mnemonic)
    return destBin

def comp2bin(mnemonic):
    # returns the binary code for the comp part of a C-instruction
    compTable = {
        "0": "0101010",
        "1": "0111111",
        "-1": "0111010",
        "D": "0001100",
        "A": "0110000",
        "!D": "0001101",
        "!A": "0110001",
        "-D": "0001111",
        "-A": "0110011",
        "D+1": "0011111",
        "A+1": "0110111",
        "D-1": "0001110",
        "A-1": "0110010",
        "D+A": "0000010",
        "D-A": "0010011",
        "A-D": "0000111",
        "D&A": "0000000",
        "D|A": "0010101",

        "M": "1110000",
        "!M": "1110001",
        "-M": "1110011",
        "M-1": "1110010",
        "D+M": "1000010",
        "D-M": "1010011",
        "M-D": "1000111",
        "D&M": "1000000",
        "D|M": "1010101",
        "M+1": "1110111"
    }

    compBin = compTable.get(mnemonic)
    return compBin

def jump2bin(mnemonic):
    # returns the binary code for the jump part of a C-instruction
    jumpTable = {
        "null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111"
    }

    jumpBin = jumpTable.get(mnemonic)
    return jumpBin
    
def commandType(command):
    # returns "A_COMMAND", "C_COMMAND", or "L_COMMAND"
    # depending on the contents of the 'command' string

    commandType = 'C_COMMAND'

    if ("@" in command):
        commandType = 'A_COMMAND'
    elif ("(" in command) and (")" in command):
        commandType = "L_COMMAND"

    return(commandType)

def getSymbol(command):
    # given an A_COMMAND or L_COMMAND type, returns the symbol as a string,
    # eg (XXX) returns 'XXX'
    # @sum returns 'sum'
    
    symbol = command.replace("@",'')
    symbol = symbol.replace("(",'')
    symbol = symbol.replace(")",'')

    return symbol


def getDest(command):
    # return the dest mnemonic in the C-instruction 'commmand'
    if ("=" in command):
        indx = command.find("=")
        mnemonic = command[:indx]
    else:
        print("No destination")
        return
    return mnemonic

def getComp(command):
    # return the comp mnemonic in the C-instruction 'commmand'
    if ((";" in command) and ("=" in command)):
        leftIndx = command.find("=")
        rightIndx = command.find(";")
        mnemonic = command[leftIndx+1:rightIndx]
        return mnemonic
    elif (";" in command):
        indx = command.find(";")
        mnemonic = command[:indx]
        return mnemonic
    elif ("=" in command):
        indx = command.find("=")
        mnemonic = command[indx+1:]
        return mnemonic
    else:
        return command

def getJump(command):
    # return the jump mnemonic in the C-instruction 'commmand'
    if (";" in command):
        indx = command.find(";")
        mnemonic = command[indx+1:]
    else:
        print("No Jump")
        return
    return mnemonic

    

def test():
    commands = ["D=D+A","D;JGT"]

    for command in commands:
        print(command)
        print("Dest: ",getDest(command), " Binary: ",dest2bin(getDest(command)))
        print("Comp: ",getComp(command), " Binary: ",comp2bin(getComp(command)))
        print("Jump: ",getJump(command), " Binary: ",jump2bin(getJump(command)))
        print()
    

