# trying out my first object oriented approach

class StackedList:
	def __init__(self):
		self.__myList = []

	def push(self, val):
		self.__myList.append(val)

	def pop(self):
		val = self.__myList[-1]
		del self.__myList[-1]
		return val 

class SumObjects(StackedList):
	def __init__(self):
		StackedList.__init__(self)
		self.__sum = 0

	def push(self, val):
		self.__sum += val
		StackedList.push(self, val)

	def pop(self):
		val = StackedList.pop(self)
		self.__sum -= val
		return val 

	def getSum(self):
		return self.__sum

randomObject = SumObjects()

cnt = 0 

for i in range(10):
	if i % 2 != 0:
		continue
	else:
		cnt += 1
		randomObject.push(i)


print(randomObject.getSum())

for i in range(cnt):
	print(randomObject.pop())
