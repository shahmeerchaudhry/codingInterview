import os

def main():
	incprice = int(input())
	percentage = int(input())

	exclusive = calc(incprice, percentage/100)
	
	print(exclusive)




def calc(incprice, percentage):
	return ((incprice/(1+percentage)))


main()