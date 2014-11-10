#include <stdio.h>

int		sum(char *str)
{
	int		result;

	result = 0;
	while (*str && *str != '-')
	{
		result += *str;
		str++;
	}
	return (result);
}

int		ft_strlen(char *str)
{
	int		len;

	len = 0;
	while (str[len] && str[len] != '-')
		len++;

	return (len);
}

void	check_sec(char *str)
{
	int		i;

	i = 0;
	while (ft_strlen(str) == 6 && sum(str) == 564)
	{
		i++;
		str += ft_strlen(str);
		if (*str == '-')
			str++;
	}
	if (!*str && *(str - 1) != '-' && i == 6)
		printf("OK NICE");
	else
		printf("NOP");
}

int		main(int argc, char *argv[])
{
	if (argc)
	{
		check_sec(argv[1]);
	}
	return (0);
}
