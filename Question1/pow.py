import os

def main():
	
	base = int(input())
	power = int(input())

	output = powSimple(base, power)

	print(output)


	output2 = powIterative(base, power);
	print("Iterative " + str(output2))c


def powSimple(base , power):
	return base ** power

def powIterative(base, power):
	i = 0
	result = 1

	for i in range (power):
		result *= base;

	return result

main()