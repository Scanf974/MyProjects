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

void	ft_bzero(char *buffer, int n)
{
	int		i;

	i = 0;
	while (i < n)
	{
		buffer[i] = 0;
		i++;
	}
}

void	ft_mult(char *n1, char *n2)
{
	char	*dest;
	int		len1 = ft_strlen(n1);
	int		l1;
	int		len2 = ft_strlen(n2);
	int		len_dest;
	int		ld_save;
	int		i;
	int		line;
	char	reste;

	len_dest = len1 + len2;
	l1 = len1;
	ld_save = len_dest;
	dest = (char *)malloc(sizeof(char) * (len_dest));
	ft_bzero(dest, len_dest);
	len1--;
	len2--;
	len_dest--;

	line = 0;
	while (len2 >= 0)
	{
		len1 = l1 - 1;
		reste = 0;
		len_dest = ld_save - 1;
		while (len1 >= 0)
		{
			dest[len_dest - line] += (n1[len1] - '0') * (n2[len2] - '0') + reste;
			reste = dest[len_dest - line] / 10;
			dest[len_dest - line] %= 10;
			len1--;
			len_dest--;
		}
		dest[len_dest - line] += reste;
		len2--;
		line++;
	}
	i = 0;
	while (dest[i] == 0)
		i++;
	while (i < ld_save)
	{
		ft_putchar(dest[i] + '0');
		i++;
	}
}

void		ft_prev(char *n1, char *n2)
{
	int		neg;

	neg = 0;
	if (n1[0] == '0' || n2[0] == '0')
		ft_putchar('0');
	else
	{
		if (n1[0] == '-')
		{
			neg = !neg;
			n1++;
		}
		if (n2[0] == '-')
		{
			neg = !neg;
			n2++;
		}
		if (neg)
			ft_putchar('-');
		ft_mult(n1, n2);
	}
}

int		main(int ac, char **av)
{
	(void)av;
	if (ac == 3)
	{
		ft_prev(av[1], av[2]);
	}
	write(1, "\n", 1);
	return (0);
}
