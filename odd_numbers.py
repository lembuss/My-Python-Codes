# prints out odd numbers

print("""
This program prints all the odd numbers between a range of the user's choice.
Enter -1 on any input to end the loop. 
""")

a = 1

while a!=-1:
    a = int(input("Please enter starting point of range: "))
    b = int(input("Please enter ending point of range: "))

    for i in range(a, b):
        if i%2 != 0:
            print(i)
