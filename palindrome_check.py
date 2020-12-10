# palindrome check 

text = input("Enter any text: ")

testText = ''

for le in text:
	if not ord(le) == 32:
		LE = le.lower()
	else:
		continue

	testText += LE

for i in range(len(testText)):
	ch = i + 1
	if testText[i] == testText[-ch]:
		continue
	else:
		print("Not a palindrome")
		break

if ch >= len(testText):
	print("Palindrome")

