import os


def main():
	
	word = str(input())
	firstLetter = word[0]

	#Send the non first letter word
	replaceCharword = replaceChar(word[1:])

	adjCollapseword = adjCollapse(replaceCharword)

	finalCode = removeNonDigits(adjCollapseword, firstLetter)

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


	#Remove all instances of W,w or H,h as
	#they do no effect the final output 

	word = word.replace("W","")
	word = word.replace("H","")
	word = word.replace("h","")
	word = word.replace("w","")

	#also get rid of spaces assuming they have no effect
	word = word.replace(" ","")


	#Iterate Through the Words and Replace with Digit

	for letter in word:
		for point, value in pointSystem.items():
			if letter in value:
				word = word.replace(letter, str(point))

	return word

def adjCollapse(word):

	new_word = ""
	prev_char = None

	#simplified adj check
	#iterates through string
	#appends  char to  string only if next char
	#is not the same as previous char

	for char in word:
		if char != prev_char:
			new_word += char
			prev_char = char
	
	return new_word

def removeNonDigits(word, firstLetter):

	#add the first letter again
	word = firstLetter + word;

	#Remove non digits defined as 0
	word = word.replace("0","");

	#Add 0s to make size 4
	while (len(word) < 4):
		word += "0"
	#If larger than 4 truncate
	if (len(word) > 4):
		word = word[0:4]

	return word

main()