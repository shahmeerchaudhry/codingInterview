import os


def main():
	word = str(input())

	replaceCharword = replaceChar(word)

	adjCollapseword = adjCollapse(replaceCharword)

	finalCode = removeNonDigits(adjCollapseword)

	print(finalCode)


def replaceChar(word):

	pointSystem = {
	0: ['A','E','I','O','U','Y','a','e','i','o','u','y'],
	1: ['B','F','P','V','b','f','p','v'],
	2: ['C','G','J','K','Q','S','X','Z','c','g','j','k','q','s','x','z'],
	3: ['D','T','d','t'],
	4: ['L','l'],
	5: ['M','N','m','n'],
	6: ['R','r']
	}

	#Iterate Through the Words and Replace with Point
	#Do not iterate on the first letter as we do not change it
	for letter in word[1:]:
		for point, value in pointSystem.items():
			if letter in value:
				word = word.replace(letter, str(point))



	#Remove all instances of W,w or H,h as
	#they do no affect the final output 

	word = word.replace("W","")
	word = word.replace("H","")
	word = word.replace("h","")
	word = word.replace("w","")

	#also get rid of spaces
	word = word.replace(" ","")

	return word

def adjCollapse(word):

	new_word = word;

	#check from first letter to last
	for i in range(len(word) - 1):
		if word[i] == word[i+1]:
			new_word = word[:i] + word[i+1:]
	return new_word

def removeNonDigits(word):

	#Remove non digits
	word = word.replace("0","");

	#Add 0 o
	while (len(word) < 4):
		word += "0"

	if (len(word) > 4):
		word = word[0:4]

	return word

main()