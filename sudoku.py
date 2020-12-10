# sudoku 


def columnSort(row):
	global columns

	for i in range(len(row)):

		indie = list(row[i])

		for j in range(len(indie)):
			a = indie[j]
			sudoku_columns[j].append(a)

	columns = []

	for i in range((len(sudoku_columns))):
		a = "".join(sudoku_columns[i]) 
		columns.append(a)


def numberCheck(row):

	global cnt 

	indie = list(row)

	for i in range(len(indie)):
		for j in range(len(indie)):
			if i == j:
				continue
			else:
				if int(indie[i]) == int(indie[j]):
					cnt = 1
					break
				else:
					continue
	return cnt



sudoku_rows = []
sudoku_columns = []
 
i = 0

while i < 9:
	
	number = input("Enter your sudoku numbers: ")

	sudoku_rows.insert(i, number)

	sudoku_columns.append([])

	i += 1

columnSort(sudoku_rows)

# print(columns)

cnt = 0

for i in range(len(sudoku_rows)):

	numberCheck(sudoku_rows[i])
	numberCheck(columns)

	
if cnt != 0:
	print("No")
else:
	print("Yes")






