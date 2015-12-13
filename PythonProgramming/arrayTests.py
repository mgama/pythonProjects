from ArraysOperations import ArraysOperations

def test1_differentArrays(): 
	arrayOperations = ArraysOperations()
	assert arrayOperations.arraysHaveSameNumbers([5,3,2,1], [5,3,2,4]) == False

def test2_equalArrays_equalOrder(): 
	arrayOperations = ArraysOperations()
	assert arrayOperations.arraysHaveSameNumbers([5,3,2,1], [5,3,2,1]) == True

def test3_equalArrays_reversedOrder(): 
	arrayOperations = ArraysOperations()
	assert arrayOperations.arraysHaveSameNumbers([5,3,2,1], [1,2,3,5]) == True

def test4_differentArrays(): 
	arrayOperations = ArraysOperations()
	assert arrayOperations.arraysHaveSameNumbers([5,3,2,1], [1,3,2,4]) == False

def test5_arrayWithDuplicates():
	arrayOperations = ArraysOperations()
	assert arrayOperations.arrayHasUniqueNumbers([1,2,3,4,5,6,7,8,9,10,1]) == False

def test6_arrayWithNoDuplicates():
	arrayOperations = ArraysOperations()
	assert arrayOperations.arrayHasUniqueNumbers([1,2,3,4,5,6,7,8,9,10,11]) == True