import sys
import os 
from pass1 import Pass1
from hackAPI import *

next_Ram = 16

symbols = {
         "R0" :  "0",
         "R1" :  "1",
         "R2" :  "2",
         "R3" :  "3",
         "R4" :  "4",
         "R5" :  "5",
         "R6" :  "6",
         "R7" :  "7",
         "R8" :  "8",
         "R9" :  "9",
         "R10" :  "10",
         "R11" :  "11",
         "R12" :  "12",
         "R13" :  "13",
         "R14" :  "14",
         "R15" :  "15",
         "SCREEN" : "16384",
         "KBD" :  "24576",
         "SP" : "0",
         "LCL" :  "1",
         "ARG" : "2",
         "THIS" : "3",
         "THAT" : "4"
}





def processA(line,lineNo,nextRAM):
    # Convert an A-instruction line of assmebly to a binary code that is 
    # 0 followed by a 15 bit address. Will use the symbol table to lookup
    # a symbol and replace it with a value. If label is not is symbol table
    # add it with correct RAM address (next in sequence)
    # Note: mini-format langauge is helpful
    binary = '0'
    line = line.replace(" ","")
    symbol = getSymbol(line)
    if symbol in symbols:
        num = int(symbols.get(symbol))
        binary += format(num, "015b")
        return binary
    else:
        symbols.update({symbol:nextRAM})
        num = nextRAM
        binary += format(num,"015b")
        global next_Ram
        next_Ram += 1
        return binary
    


def processC(line):
    # Convert a C-instruction line of code to the correct computation,destination, 
    # and jump binary codes. These should be preceded by 111, which signifies the
    # C-instruction
    line = line.replace(" ","")

    binary = "111"

    dest = getDest(line)
    cmp = getComp(line)
    jmp = getJump(line)

    #111accccccdddjjj
    binary += comp2bin(cmp)
    binary += dest2bin(dest)
    binary += jump2bin(jmp)

    return binary

def processL(line,lineNo):
    # When an L-Instruction (label in the form (LABEL)) is encountered, 
    # the label should be placed into the symbol table with the correct line
    line = line.replace(" ","")
    nextLine = lineNo + 1
    symbol = getSymbol(line)
    cleanSymbol = symbol.rstrip('\n')
    symbols.update({cleanSymbol:nextLine})

def clean_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    cleaned_lines = []

    for line in lines:
        line = line.strip()  # remove leading/trailing white space
        if not line.startswith('//') and line != '':  # ignore comment lines and empty lines
            if '//' in line:  # if the line has a comment
                line = line.split('//')[0]  # keep only the part before the comment
                line = line.strip()  # remove any extra white space
            cleaned_lines.append(line)

    newFile = 'cleaned_file.txt'

    with open(newFile, 'w') as f:
        f.write('\n'.join(cleaned_lines))

    return newFile
    

def pass_1(file):
    # scan each line of file and find L_COMMANDS
    # place them in the symbol table with appropriate ROM numbers
    file = clean_file(file)
    with open(file,'r') as f:
        lines = f.readlines()

    lineNo = 1
    for line in lines:
        if commandType(line) == "L_COMMAND":
            processL(line,lineNo)
        lineNo += 1

    pass_2(lines)
            


def pass_2(file):
    # Scan file and write correct binary code to stdout.
    # Hint: file.seek(0) resets the file pointer for another pass
    out = open('out.hack','w')


    lineNo = 1
    global next_Ram
    for line in file:
        line = line.rstrip('\n')
        if commandType(line) == "A_COMMAND":
            out.write(processA(line,lineNo,next_Ram)+'\n')
        elif commandType(line) == "C_COMMAND":
            out.write(processC(line)+'\n')
        else:
            continue




path = sys.argv[1] #get file name from command line 

if (os.path.exists(path)): #check if file name exists
    pass_1(path)
    print(symbols)


else:
    print("File does not exist") #end program and throw error
    exit()

