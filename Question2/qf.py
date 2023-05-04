import os
import math


def main():
	a = int(input())
	b = int(input())
	c = int(input())

	quadratic(a, b ,c)




def quadratic(a,b,c):

	a,b,c = a,b,c;

	#x1 output
	x1 = ((- b + squareroot(a,b,c)) / (2 * a))
	print(x1)

	#x2 output
	x2 = ((- b - squareroot(a,b,c)) / (2 * a))
	print(x2)


#Squareroot Calculator Must Return greater than 0
def squareroot(a,b,c):
	ans = math.sqrt(( (b**2) - (4 * a * c )))
	return ans

main()