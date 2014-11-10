#ifndef __HUIT_H__
# define __HUIT_H__

# include "ft.h"


# define TRUE	1
# define FALSE	0
typedef int		t_bool;

int		fn(int nb);
void	init(int map[8][8]);
void	print_tab(int map[8][8]);
t_bool	abs_global(int map[8][8], int y0, int x0);

#endif
