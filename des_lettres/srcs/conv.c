int		conv(char *str)
{
	int		signe;
	int		nombre;

	nombre = 0;
	signe = 1;
	if (*str == '-')
	{
		signe = -1;
		str++;
	}
	while (*str)
	{
		nombre = (10 * nombre) + (*str - '0');
		str++;
	}
	return (signe * nombre);
}
