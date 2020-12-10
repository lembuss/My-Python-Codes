# program alculates the sum of numbers in an array

elem = int(input("How many elements should the array have? "))

array = []

total = 0

for i in range(elem):
    nextElement = int(input("Enter the next element: "))
    array.append(nextElement)    
    total += nextElement

print("Your array is: ", array)
print("The sum of elements in your array is: ", total )
    
    
