# my own caesar cypher


text = input("Enter your message: ")

cipher = ''

for le in text:
	if not le.isalpha():
		continue

	LE = le.upper()
	code = ord(LE) + 1

	if code > ord('Z'):
		code = ord('A')

	LE = chr(code)

	cipher += LE


print(cipher)
