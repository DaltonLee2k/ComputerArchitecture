def _getPushMem(src):
    #take whats in local and push it to the stack
    # INPUT: src - a text string that is a symbol corresponding to a RAM address containing an address
    # OUTPUT: a text string that will result in the address in src being pushed 
    # to the top of the stack. 
    pass

def _getPushLabel(src):
    # INPUT: src - a text string that is some label, eg '(MAIN_LOOP)' which 
    # corresponds to a ROM address in the symbol table.
    # OUTPUT: a text string that will result in the ROM address 
    # to the top of the stack.
    pass

def _getPopMem(dest):
    # something from teh stack to specific location
    # INPUT: src - a text string that is a symbol that corresponding to a RAM address containing an address
    # OUTPUT: a text string that pops the stack and places that value into the dest segment pointer
    pass

def _getMoveMem(src,dest):
    #Move somethings thats in one space into another
    # INPUT: src - a text string that is a symbol corresponding to a RAM address containing an address
    # INPUT: dest- a text string that is a symbol corresponding to a RAM address containing an address
    # OUPUT: a text string that copies the address in src to dest
    pass