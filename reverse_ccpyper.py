# my own caesar cypher


cipher = input("Enter your encrypted message: ")

text = ''

for le in cipher:
	if not le.isalpha():
		continue

	LE = le.upper()
	code = ord(LE) - 1

	if code < ord('A'):
		code = ord('Z')

	LE = chr(code)

	text += LE


print(text)
