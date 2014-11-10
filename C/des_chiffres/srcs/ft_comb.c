#include "../includes/chiffre.h"

int		*ft_intcpy(int *dest, int *src, int len)
{
	int		i;

	i = 0;
	while (i < len)
	{
		dest[i] = src[i];
		i++;
	}
	return (dest);
}

void	print_tab(int *tab, int len)
{
	int		i;

	for (i = 0; i < len; i++)
	{
		ft_putnbr(tab[i]);
		ft_putstr(" ");
	}
	ft_putchar('\n');
}

int		*ft_swap(int *tab, int pos1, int pos2)
{
	int		save;

	save = tab[pos1];
	tab[pos1] = tab[pos2];
	tab[pos2] = save;
	return (tab);
}

void	ft_comb(int *tab, int len, int cursor, int real)
{
	int		i;

	if (len - cursor <= 1)
	{
		if (ft_opp(tab[0], 1, tab ,real) == real)
			ft_putstr("Le compte est bon\n\n");
	}
	else
	{
		i = cursor;
		while (i < len)
		{
			ft_swap(tab, i, cursor);
			ft_comb(tab, len , cursor + 1, real);
			ft_swap(tab, i, cursor);
			i++;
		}
	}
}
