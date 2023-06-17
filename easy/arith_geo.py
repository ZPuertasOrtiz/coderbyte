def arithGeo (arr):
    difference = arr[0]-arr[1]
    multiplied = int(arr[1]/arr[0])
    
    for i in range(1,len(arr)-1):
        if arr[i]-arr[i+1]==difference:
            pattern = "Arithmetic"
        else:
            pattern = -1
            break
    
    if pattern != "Arithmetic":    
        for i in range(1,len(arr)-1):
            if arr[i+1]/arr[i]==multiplied:
                pattern = "Geometric"
            else: 
                pattern = -1
                break
            
    return pattern 



            
    
    
            
    
    
    
    
    
    
    
    
    