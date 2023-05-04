#include <iostream>
#include <math.h>
using namespace std;



int powRecursive(int b, int p)
{
	if (p == 0)
	{
		return 1;
	}
	else if (p == 1)
	{
		return b;
	}
	else
	{
		return b * powRecursive(b, p - 1);
	}

}

int powIterative(int b, int p)

{
	int result= 1;
	int i = 0;

	while (i < p)
	{
		result *= b ;
		i++;
	}

	return result;
}





int main()
{

	int b, p;

	cin >> b;
	cin >> p;

	cout << "Using Pow " << pow(b, p) << endl;

	cout <<  "Recursive " << powRecursive(b, p) << endl;

	cout << "Iterative " << powIterative(b, p) << endl;
}
