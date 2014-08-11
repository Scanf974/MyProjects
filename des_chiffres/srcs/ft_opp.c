#include "../includes/chiffre.h"

int		ft_opp(int result, int index, int *tab, int real_res)
{
	if (index == 6 || result == real_res)
		return (result);
	if (ft_opp(result + tab[index], index + 1, tab, real_res) == real_res)
	{
		print_plus(result, tab, index);
		return (real_res);
	}
	else if (ft_opp(result - tab[index], index + 1, tab, real_res) == real_res)
	{
		print_moins(result, tab, index);
		return (real_res);
	}
	else if (ft_opp(result * tab[index], index + 1, tab, real_res) == real_res)
	{
		print_mult(result, tab, index);
		return (real_res);
	}
	else if (tab[index] && result % tab[index] == 0
			&& ft_opp(result / tab[index], index + 1, tab, real_res) == real_res)
	{
		print_div(result, tab, index);
		return (real_res);
	}
	return (0);
}
