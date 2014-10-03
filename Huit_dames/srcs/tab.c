#include "../includes/huit.h"

void	init(int map[8][8])	
{
	int		y;
	int		x;

	y = 0;
	while (y < 8)
	{
		x = 0;
		while (x < 8)
		{
			map[y][x] = 0;
			x++;
		}
		y++;
	}
}

void	print_tab(int map[8][8])
{
	int		y;
	int		x;

	y = 0;
	while (y < 8)
	{
		x = 0;
		while (x < 8)
		{
			ft_putnbr(map[y][x]);
			ft_putchar(' ');
			x++;
		}
		ft_putchar('\n');
		y++;
	}
}
