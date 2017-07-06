#Fibonacci Sequence
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34
#Create a class that will return an fibonacci number from the sequence

class fibonacci: 

	def __init__(self):
		self.fibonacciSeq = []
		self.F_n = 0
		self.F_n2 = 1
	
	def generateSequence(self, number):
		if number == 1:
			return self.F_n
		if number == 2:
			return self.F_n2
		else:
			self.fibonacciSeq = [self.F_n, self.F_n2]
			print self.fibonacciSeq
			for i in range(2, number):
				self.fibonacciSeq.append(self.F_n + self.F_n2)
				#print "The sequence inside for loop is " + str(self.fibonacciSeq)
				#print "i has a value of " + str(i)
				self.F_n = self.F_n2
				self.F_n2 = self.fibonacciSeq[i]
			return self.fibonacciSeq

	def getFibonacciNumber(self, number):
		self.generateSequence(number)
		return self.fibonacciSeq[number - 1]


if __name__ == '__main__':
	f = fibonacci()
	print f.generateSequence(10)

