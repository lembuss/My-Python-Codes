# my own caesar cypher


text = input("Enter your message: ")
diff = int(input("What should be the shift range? (Enter a number between 1-25) "))

cipher = ''

for le in text:
	# leave the nno- alphabetic characters as they are
	if not le.isalpha():
		LE = le

	# work with upper characters
	if le.isupper():
		code = ord(le) + diff

		if code > ord('Z'):
			upperDiff = code - ord('Z') - 1
			code = ord('A')	+ upperDiff

		LE = chr(code)

	if le.islower():
		code = ord(le) + diff	

		if code > ord('z'):
			lowerDiff = code - ord('z') - 1
			code = ord('a')	+ lowerDiff	
		
		LE = chr(code)

	cipher += LE


print(cipher)
