def arrayAdditionI(arr):
    maximum = max(arr)
    arr.remove(maximum)
    arr.sort()
    print(arr)
    #este for controla el primer numero
    for i in range(len(arr)):
        
        jump=1
        #el jump va rodando un intervalo por ej [1, 2, 3], salta dos y sigue
        while jump<= len(arr)-1:
            print(jump)
            addition =1
            while i+addition < len(arr):
                # print(i+addition)
                # print("...................")
                comparison = sum(arr[i:i+addition:jump])
                print(arr[i:i+addition:jump])
                # print("------------------")
                #este for es para la suma de uno por uno
                for j in range (i+addition, len(arr)):
                    print(comparison + arr[j])
                    print("*******")
                    if comparison + arr[j]==maximum:
                        return True
                addition+=1
            jump +=1
    return False


        
print(arrayAdditionI([4, 6, 230, 10, 1, 3,201,9]))