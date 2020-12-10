# digit of life
def digitSum (digits):

	dig = []
	initSum = 0 
	for i in range(len(digits)):
		d = int(digits[i])
		dig.append(d)
		initSum += dig[i]	

	return initSum

dob = input("Enter your date of birth in the format DDMMYYYY: ")

digits = list(dob)


initSum = digitSum(digits)


print(initSum)
while True:
	if initSum < 10:
		print("Your digit of life is ", initSum)
		break
	else:
		digits = str(initSum)
		initSum = digitSum(digits)

 