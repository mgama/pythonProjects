from .context import PythonProgramming

def test1_differentArrays(): 
	arrayOperations = ArraysOperations()
	print "From test1_differentArrays"
	print arrayOperations.arraysHaveSameNumbers([5,3,2,1], [5,3,2,4])
	assert arrayOperations.arraysHaveSameNumbers([5,3,2,1], [5,3,2,4]) == False

def test2_equalArrays_equalOrder(): 
	arrayOperations = ArraysOperations()
	print "From test2_equalArrays_equalOrder"
	print arrayOperations.arraysHaveSameNumbers([5,3,2,1], [5,3,2,1])
	assert arrayOperations.arraysHaveSameNumbers([5,3,2,1], [5,3,2,1]) == True

def test3_equalArrays_reversedOrder(): 
	arrayOperations = ArraysOperations()
	print "From test3_equalArrays_reversedOrder"
	print arrayOperations.arraysHaveSameNumbers([5,3,2,1], [1,2,3,5])
	assert arrayOperations.arraysHaveSameNumbers([5,3,2,1], [1,2,3,5]) == True

def test4_differentArrays(): 
	arrayOperations = ArraysOperations()
	print "From test4_differentArrays"
	print arrayOperations.arraysHaveSameNumbers([5,3,2,1], [1,3,2,4])
	assert arrayOperations.arraysHaveSameNumbers([5,3,2,1], [1,3,2,4]) == False

def test5_arrayWithDuplicates():
	arrayOperations = ArraysOperations()
	print "From test5_arrayWithDuplicates"
	print arrayOperations.arrayHasUniqueNumbers([1,2,3,4,5,6,7,8,9,10,1])
	assert arrayOperations.arrayHasUniqueNumbers([1,2,3,4,5,6,7,8,9,10,1]) == False

def test6_arrayWithNoDuplicates():
	arrayOperations = ArraysOperations()
	print "From test6_arrayWithNoDuplicates"
	print arrayOperations.arrayHasUniqueNumbers([1,2,3,4,5,6,7,8,9,10,11])
	assert arrayOperations.arrayHasUniqueNumbers([1,2,3,4,5,6,7,8,9,10,11]) == True