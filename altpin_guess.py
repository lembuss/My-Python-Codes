# Program tries to guess your 4 digit pin 

pin = int(input("Enter your 4 digit pin. The program will try and guess it: \n"))
step = 0

for i in range(0, 10000):
    if i == pin:
        print("Your pin is ", i, "\n")
        break
    else:
        step += 1
        continue

print("It took ",step," steps")

