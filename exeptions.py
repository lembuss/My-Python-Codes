def readint(prompt, min, max):
    
    
    try:
        type(prompt) == int
    except:
        print("Error: wrong input")
        
    if prompt in range(min, max):
        print("The number is: ", prompt)
        return False
    else:
        print("Error: the value is not within permitted range (-10..10)") 
    
        
while True:
    v = input("Enter a number from -10 to 10: ")
    readint(v, -10, 10)


print("The number is:", v)
