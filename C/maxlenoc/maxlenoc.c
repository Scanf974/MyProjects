#include <unistd.h>
#include <stdlib.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_putstr(char *str)
{
	while (*str)
		write(1, str++, 1);
}

int		ft_strlen(char *str)
{
	int		i;

	i = 0;
	while (str[i])
		i++;
	return (i);
}

char	*ft_strncpy(char *dst, char *str, int n)
{
	int		i;

	i = 0;
	while (str[i] && i < n)
	{
		dst[i] = str[i];
		i++;
	}
	dst[i] = 0;
	return (dst);
}

int		ft_strstr(char *s1, char *s2)
{
	int		i;
	int		j;

	i = 0;
	while (s2[i])
	{
		j = 0;
		while (s2[i + j] && s1[j] && s2[i + j] == s1[j])
			j++;
		if (s1[j] == 0)
			return (1);
		i++;
	}
	return (0);
}

int		ft_lenoc(char **av)
{
	char	*first;
	int		i;
	int		e;
	int		save;
	int		start;
	int		len;

	len = ft_strlen(av[0]);
	first = (char *)malloc(sizeof(char) * (len + 1));
	save = len;
	while (len > 0)
	{
		e = save;
		start = 0;
		while (e >= len) 
		{
			first = ft_strncpy(first, &av[0][start], len);
			start++;
			e--;
			i = 1;
			while (av[i] && ft_strstr(first, av[i]))
				i++;
			if (!av[i])
			{
				ft_putstr(first);
				return (1);
			}
		}
		e++;
		len--;
	}
	return (0);
}

int	main(int ac, char **av)
{
	if (ac >= 2)
		ft_lenoc(++av);
	write(1, "\n", 1);
	return (0);
}
