

def abCheck(str):
    pos_a = str.find("a")
    pos_b = str.find("b")
    return True if abs(pos_a - pos_b) == 4 else False
        
    
    
print(abCheck(''))