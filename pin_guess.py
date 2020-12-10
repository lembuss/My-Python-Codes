# Program tries to guess your 4 digit pin 

pin = int(input("Enter your 4 digit pin. The program will try and guess it: \n"))

x = [int(d) for d in str(pin)]

guess = [0]*4

step = 0

for i in range(0,10):
    if i == x[0]:
        guess[0] = i
        break
    else:
        step += 1
        continue

for j in range(0,10):
    if j == x[1]:
        guess[1] = j
        break
    else:
        step += 1
        continue

for k in range(0,10):
    if k == x[2]:
        guess[2] = k
        break
    else:
        step += 1
        continue

for l in range(0,10):
    if l == x[3]:
        guess[3] = l        
        break
    else:
        step += 1                                
        continue

print("It took ", step, " steps to determine your number: " )


#for i in guess:
#    print(i, end="")

pin_guess = guess[0]*10**3 + guess[1]*10**2 + guess[2]*10 + guess[3] 

print(pin_guess)

print("\n")

