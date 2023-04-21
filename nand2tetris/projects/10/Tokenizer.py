import re

class Tokenizer:
    def __init__(self, file):
        self.keywords = ['boolean', 'char', 'class', 'constructor', 'do', 'else', 'false', 'field', 'function', 'if', 'int', 'let', 'method', 'null', 'return', 'static', 'this', 'true', 'var', 'void', 'while']
        self.symbols = '{}()[].,;+-*/&|<>=~'
        self.numberChars = '0123456789'
        self.numberStart = self.numberChars
        self.identStart = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
        self.identChars = self.identStart + self.numberChars
        
        self.file = self.clean_file(file)
        with open(self.file, 'r') as f:
            self.lines = f.readlines()
        self.tokens = []
        self.currentTokenIndex = 0
        self.tokenize()

    def clean_file(self, file):
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
    
    def hasMoreTokens(self):
        return self.currentTokenIndex < len(self.tokens)

    def advance(self):
        if self.hasMoreTokens():
            self.currentTokenIndex += 1

    def tokenType(self):
        token = self.token()
        if token in self.keywords:
            return "KEYWORD"
        elif token in self.symbols:
            return "SYMBOL"
        elif token[0] in self.numberChars:
            return "INT_CONST"
        elif token[0] in self.identStart:
            return "IDENTIFIER"
        elif token[0] == '"':
            return "STRING_CONST"
        else:
            raise Exception("Invalid token: " + token)

    def token(self):
        return self.tokens[self.currentTokenIndex]

    def tokenize(self):
        for line in self.lines:
            #splits line from cleaned file based on characters
            words = re.findall(r'[{}()[\].,;+\-*/&|<>=~]|".+?"|\w+', line) #from https://stackoverflow.com/questions/40734235/how-to-use-re-findall-in-python
            #\w strings of words to be returned as a single word
            for word in words:
                self.tokens.append(self.getToken(word))

    def getToken(self, symbol):
        if symbol == "<":
            return("<symbol>"+"&lt;"+"</symbol>")
        if symbol == ">":
            return("<symbol>"+"&gt;"+"</symbol>")
        
        #determine XML output based on Token
        if symbol in self.keywords:
            return("<keyword>"+symbol+"</keyword>")
        elif symbol in self.symbols:
            return("<symbol>"+symbol+"</symbol>")
        elif symbol[0] in self.numberChars:
            return("<integerConstant>"+symbol+"</integerConstant>")
        elif symbol[0] in self.identStart:
            return("<identifier>"+symbol+"</identifier>")
        elif symbol[0] in self.numberChars:
            return("<intConst>"+symbol+"</intConst>")
        elif symbol[0] == '"':
            symbol = symbol.strip('"')
            return("<stringConstant>"+symbol+"</stringConstant>")
        else:
            return(symbol)
