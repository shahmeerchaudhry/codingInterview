powIterative(3,2);

function powIterative(base, power)
{
	i = 0;
	result = 1;
	while (i < power)
	{
		result *= base;
		i++;
	}

	console.log(result);
}
