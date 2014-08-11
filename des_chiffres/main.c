#include "includes/chiffre.h"

int		main(int argc, char *argv[])
{
	int		i;
	int		tab[6];
	int		real;

	i = 0;
	if (argc == 8)
	{
		real = conv(argv[argc - 1]);
		while (i < argc - 2)
		{
			tab[i] = conv(argv[i + 1]);
			i++;
		}
		ft_comb(tab, 6, 0, real);
	}
	return (0);
}
