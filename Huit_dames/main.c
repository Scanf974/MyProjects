#include "includes/huit.h"

int		main(void)
{
	int		map[8][8];

	init(map);
	print_tab(map);
	ft_putchar('\n');
	map[7][6] = 1;
	print_tab(map);
	ft_putnbr(abs_global(map, 7, 7));
	return (0);
}
