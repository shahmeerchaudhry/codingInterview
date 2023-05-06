//Included for testing not needed for function
#include <stdio.h>

//This assumes source and destination are same size
//Or Destination has enough space to copy source to

//Using pointers hence do not need to return anything

void copy(char *source, char *destination)
{
	int i = 0;


	//We run through source and copy each element until null pointer
	while (source[i] != '\0')
	{

		destination[i] = source[i];

		i++;
	}

	//At this point i will be the size of char in source
	//We add the null pointer to terminate the string
	destination[i] = '\0';

}


int main()
{
	char word []  = "Hello";
	char word2 [100];

	copy(word, word2);

	printf("%s", word2);
}