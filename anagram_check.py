# check if two inputs are anagrams

fT = input("Enter first text: ")

sT = input("Enter second text: ")

firstText = ''
secondText = ''

for le in fT:
	if not ord(le) == 32:
		LE = le.lower()

	firstText += LE


for le in sT:
	if not ord(le) == 32:
		LE = le.lower()

	secondText += LE

test = 0

for le in firstText:
	if le in secondText:
		test += 1
		continue
	else:
		print("Not anagrams")
		break

if test == len(firstText):
	print("Anagrams")

