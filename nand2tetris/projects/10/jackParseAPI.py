
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
    for line in lines:
        print(line)
    pass_2(lines)


def pass_2(file):
    
    pass


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