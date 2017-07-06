from nose.tools import *
from .context import PythonProgramming
from PythonProgramming import fibonacci	

def test1_getFibonacciNumber_Test():
	fib = fibonacci.fibonacci()
	assert fib.getFibonacciNumber(5) == 3

def test2_generateSequence_Test():
	fib = fibonacci.fibonacci()
	assert fib.generateSequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test3_getFibonacciNumber_Test():
	fib = fibonacci.fibonacci()
	assert fib.getFibonacciNumber(10) == 34

def test4_generateSequence_Test():
	fib = fibonacci.fibonacci()
	assert fib.generateSequence(15) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]