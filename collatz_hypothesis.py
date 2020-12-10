# trying to disprove collatz hypothesis

# c0 = int(input("Enter any non-zero and non-negative number: "))

for i in range(1,100):
    print(i)
    steps = 0
    while c0 !=1:
        if c0%2 == 0:
            c0 = c0 / 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
    else:
        print(c0)
        print("Steps taken:", steps)
        
