"""
The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

Fibonacci sequence characterized by the fact that every number after the first two is the sum of the two preceding ones:

Fibonacci(0) = 0, 
Fibonacci(1) = 1,
Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)  


Write a Python function that takes in a number N, and returns the sum of all the even-valued terms of the Fibonacci sequence

"""


class FibonacciSequence():
	def evenNumberedFibonacci(self, N):
		result=0
		temp = 0
		cur = recur(temp)
		while cur <= N:
			if cur % 2 == 0: 
				result += cur
			temp += 1
			cur = recur(temp)

		return result


def recur(s):
	if s < 0:
		print("Not Valid")
	if s == 0: 
		return(0)
	elif s == 1: 
		return(1)
	else:
		return recur(s -1) + recur(s - 2) 

	
	


s= FibonacciSequence()
s.evenNumberedFibonacci(34)






