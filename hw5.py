"""
Prime factorization is a way of expressing a number as a product of its prime factors. 
A prime number is a number that has exactly two factors, 1 and the number itself.

The prime factors of 13195 are 5, 7, 13 and 29.

Given a number 'N', return its largest prime factor.

"""


class PrimeFactor():
	def largestPrimeFactor(self, N):
		bigP = 1
		tes = 1
		for x in range(N): 
			if x != 0:
				if N % x == 0: 
					for a in range(x):
						if a != 1 and a != 0 and x % a == 0:
							tes = 0
					if tes == 0: 
						tes = 1
					else: 
						bigP = x
		return bigP




# Test your Code

s= PrimeFactor()
result =s.largestPrimeFactor(30)
r = -765432 % 38271
print(r)







