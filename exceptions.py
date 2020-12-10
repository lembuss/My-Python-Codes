def readint(prompt, min, max):
    global a 

    try:
        prompt = int(prompt)
    except:
        print("Error: wrong input")
        return
        
    if prompt in range(min, max):
        a = 6        
        return a

    else:
        print("Error: the value is not within permitted range (-10..10)") 
    
a = int(5)
        
while a == 5:
    v = input("Enter a number from -10 to 10: ")
    readint(v, -10, 10)
    if a == 5:
        continue
    else:
        break


print("The number is:", v)
