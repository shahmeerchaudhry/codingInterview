//Included for testing
#include <stdio.h>

//This assumes source and destination are same size
//Or Destination has enough space to copy source to
void copy(char *source, char *destination)
{
	int i = 0;

	while (source[i] != '\0')
	{

		destination[i] = source[i];

		i++;
	}

	destination[i] = '\0';

}

int main()
{
	char word []  = "Hello";
	char word2 [100];

	copy(word, word2);

	printf("%s", word2);
}