#include "../includes/huit.h"


t_bool		abs_line(int map[8][8], int y0)
{
	int		x;

	x = 0;
	while (x < 8)
	{
		if (map[y0][x])
			return (FALSE);
		x++;
	}
	return (TRUE);
}

t_bool		abs_col(int map[8][8], int x0)
{
	int		y;

	y = 0;
	while (y < 8)
	{
		if (map[y][x0])
			return (FALSE);
		y++;
	}
	return (TRUE);
}

t_bool		abs_diago_1(int map[8][8], int y0, int x0)
{
	int		x;
	int		y;

	y = y0;
	x = x0;
	while (y < 8 && x < 8)
	{
		if (map[y][x])
			return (FALSE);
		x++;
		y++;
	}
	while (y > 0 && x > 0)
	{
		if (map[y][x])
			return (FALSE);
		x--;
		y--;
	}
	return (TRUE);
}

t_bool		abs_diago_2(int map[8][8], int y0, int x0)
{
	int		x;
	int		y;

	y = y0;
	x = x0;
	while (y < 8 && x > 0)
	{
		if (map[y][x])
			return (FALSE);
		y++;
		x--;
	}
	while (y > 0 && x < 8)
	{
		if (map[y][x])
			return (FALSE);
		y--;
		x++;
	}
	return (TRUE);
}

t_bool		abs_global(int map[8][8], int y0, int x0)
{
	if (abs_line(map, y0) &&
			abs_col(map, x0) &&
			abs_diago_1(map, y0, x0) &&
			abs_diago_2(map, y0, x0))
		return (TRUE);
	return (FALSE);
}
