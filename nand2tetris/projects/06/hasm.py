import sys
import os 
from pass1 import Pass1

path = sys.argv[1] #get file name from command line 

if (os.path.exists(path)): #check if file name exists
    Pass1(path)

else:
    print("File does not exist") #end program and throw error
    exit()

