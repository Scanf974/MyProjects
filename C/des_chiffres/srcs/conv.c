int		conv(char *str)
{
	int		result;

	result = 0;
	while (*str)
	{
		result = result * 10 + (*str - '0');
		str++;

	}
	return (result);

}

