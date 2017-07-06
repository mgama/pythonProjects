from .context import PythonProgramming

def test1_getFibonacciNumber_Test():
	fib = Fibonacci()
	print fib.getFibonacciNumber(5)
	assert fib.getFibonacciNumber(5) == 3

def test2_generateSequence_Test():
	fib = Fibonacci()
	fib.generateSequence(10)
	print fib.generateSequence(10)
	assert fib.fibonacciSeq == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test3_getFibonacciNumber_Test():
	fib = Fibonacci()
	print fib.getFibonacciNumber(10)
	assert fib.getFibonacciNumber(10) == 34

def test4_generateSequence_Test():
	fib = Fibonacci()
	fib.generateSequence(15)
	print fib.generateSequence(15)
	assert fib.fibonacciSeq == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]