def dashInsert(str):
    new_str = list(str)
    
    
    
    for i in range(len(new_str)):
        if int(new_str[i]) % 2 != 0:
            new_str.insert(i,"-")
            print(len(new_str))
            
            i+=1
    return new_str
            
            
        
print(dashInsert('454793'))
    