import sys
import os 
from jackParseAPI import pass_1


path = sys.argv[1] #get file name from command line 

if (os.path.exists(path)): #check if file name exists
    pass_1(path)


else:
    print("File does not exist") #end program and throw error
    exit()