
import re

keywords = ['boolean', 'char', 'class', 'constructor', 'do', 'else', 'false', 'field', 'function', 'if', 'int', 'let', 'method', 'null', 'return', 'static', 'this', 'true', 'var', 'void', 'while']
symbols = '{}()[].,;+-*/&|<>=~'
numberChars = '0123456789'
numberStart = numberChars
identStart = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
identChars = identStart + numberChars


def pass_1(file):
    file = clean_file(file)
    with open(file,'r') as f:
        lines = f.readlines()
    pass_2(lines)

def getToken(symbol):
    if symbol == "<":
        return("<symbol>"+"&lt;"+"</symbol>")
    if symbol == ">":
        return("<symbol>"+"&gt;"+"</symbol>")
    
    
    #determine XML output based on Token
    if symbol in keywords:
        return("<keyword>"+symbol+"</keyword>")
    elif symbol in symbols:
        return("<symbol>"+symbol+"</symbol>")
    elif symbol[0] in numberChars:
        return("<integerConstant>"+symbol+"</integerConstant>")
    elif symbol[0] in identStart:
        return("<identifier>"+symbol+"</identifier>")
    elif symbol[0] in numberChars:
        return("<intConst>"+symbol+"</intConst>")
    elif symbol[0] == '"':
        symbol = symbol.strip('"')
        return("<stringConstant>"+symbol+"</stringConstant>")
    else:
        return(symbol)

def pass_2(file):
    out = open('out.xml','w')
    out.write("<tokens>\n")
    

    for line in file:
        #splits line from cleaned file based on characters
        words = re.findall(r'[{}()[\].,;+\-*/&|<>=~]|".+?"|\w+', line) #from https://stackoverflow.com/questions/40734235/how-to-use-re-findall-in-python
        #\w strings of words to be returned as a single word
        for word in words:
            out.write(getToken(word)+"\n")

    out.write("</tokens>")

        



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
            if '/*' in line:
                line = line.split('/*')[0]
                line = line.strip()
            if "*/" in line:
                line = line.split('*/')[1]
                line = line.strip()
            cleaned_lines.append(line)

    newFile = 'cleaned_file.txt'

    with open(newFile, 'w') as f:
        f.write('\n'.join(cleaned_lines))

    return newFile