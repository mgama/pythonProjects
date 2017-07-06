#Given 2 lists of numbers, identify if they both have the same numbers or not. It does not matter the order
#but it should detect if they are duplicates in any of the two

class arrays_operations: 

	def __init__(self):
		self.arraysAreEqual = False

	def arraysHaveSameNumbers(self, array1, array2):
		reasonMessage = ""
		if (self.arrayHasUniqueNumbers(array1) == True and self.arrayHasUniqueNumbers(array2) == True): 
			for i in array1: 
				if i in array2: 
					# print str(i) + " from array 1 is inside array 2"
					self.arraysAreEqual = True
				else:
					# print str(i) + " from array 1 is not on array 2"
					self.arraysAreEqual = False
					reasonMessage = " Because the number " + str(i) + " from array 1 is not on array 2"
					break
			print "The arrays have the same numbers? " + str(self.arraysAreEqual) + reasonMessage
		else:
			print "At least one of the arrays has duplicate numbers inside"
		return self.arraysAreEqual

	def arrayHasUniqueNumbers(self, array):
		# print "The length of the array is " + str(len(array))
		for fixedElement in range(0, len(array)):
			# print "The fixedElement is " + str(fixedElement)
			for element in range(fixedElement + 1, len(array)):
				# print "element " + str(element)
				# print "comparing " + str(array[fixedElement]) + " with " + str(array[element])
				if (array[fixedElement] == array[element]):
					print " Found duplicate: " + str(array[fixedElement]) + " and " + str(array[element])
					return False
		print 'All numbers inside the array ' + str(array) + ' are unique'
		return True

	def orderArray(self, array):
		orderedArray = []
		for i in range(len(array)):
			print i, array[i]
			for j in range(len(array)-1):
				print "Comparing " + str(array[i]) + " with " + str(array[j])

	# def retrieveLowestNumber(self, array):


	# def retrieveSecondLowestNumber(self, array):

if __name__ == '__main__':
	testArray1 = [5,3,2,1]
	testArray2 = [5,3,2,4]

	arrayOperations = arrays_operations()
	# arrayOperations.arraysHaveSameNumbers(testArray1, testArray2)
	# arrayOperations.arrayHasUniqueNumbers(testArray1)
	arrayOperations.orderArray(testArray1)