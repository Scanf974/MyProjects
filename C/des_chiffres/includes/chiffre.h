#ifndef __CHIFFRE_H__
# define __CHIFFRE_H__

# include "ft.h"

int		conv(char *str);
void	print_plus(int result, int *tab, int index);
void	print_moins(int result, int *tab, int index);
void	print_mult(int result, int *tab, int index);
void	print_div(int result, int *tab, int index);
int		ft_opp(int result, int index, int *tab, int real_res);
void	print_tab(int *tab, int len);
void	ft_comb(int *tab, int len, int cursor, int real);

#endif
