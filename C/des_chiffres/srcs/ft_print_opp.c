#include "../includes/chiffre.h"

void	print_plus(int result, int *tab, int index)
{
	ft_putnbr(result);
	ft_putstr(" + ");
	ft_putnbr(tab[index]);
	ft_putstr(" = ");
	ft_putnbr(result + tab[index]);
	ft_putstr("\n"); 
}

void	print_moins(int result, int *tab, int index)
{
	ft_putnbr(result);
	ft_putstr(" - ");
	ft_putnbr(tab[index]);
	ft_putstr(" = ");
	ft_putnbr(result - tab[index]);
	ft_putstr("\n"); 
}
void	print_mult(int result, int *tab, int index)
{
	ft_putnbr(result);
	ft_putstr(" x ");
	ft_putnbr(tab[index]);
	ft_putstr(" = ");
	ft_putnbr(result * tab[index]);
	ft_putstr("\n"); 
}
void	print_div(int result, int *tab, int index)
{
	ft_putnbr(result);
	ft_putstr(" / ");
	ft_putnbr(tab[index]);
	ft_putstr(" = ");
	ft_putnbr(result / tab[index]);
	ft_putstr("\n"); 
}
