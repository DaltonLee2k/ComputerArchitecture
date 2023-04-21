from Tokenizer import Tokenizer
import sys



# create an instance of the Tokenizer class, passing in the file name as an argument
tokenizer = Tokenizer("ArrayTest/Main.jack")

# use the class methods to tokenize the input file and get the desired output
while tokenizer.hasMoreTokens():
    tokenizer.advance()
    token_type = tokenizer.tokenType()
    token = tokenizer.token()
    # do something with the token and token_type, such as writing them to a file or printing them to the console
