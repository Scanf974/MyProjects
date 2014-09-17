#include "../includes/ist.h"


int		lines(char *str)
{
	int		len;

	len = 1;
	while (*str)	
	{
		if (*str == '\n')
			len++;
		str++;
	}
	return (len);
}

int		colones(char *str)
{
	int		i;

	i = 0;
	while (*str && *str != '\n')
	{
		i++;
		str++;
	}
	return (i);
}

char	*ft_strncpy(char *line, char *str, int nb)
{
	int		i;

	i = 0;
	while (i < nb && *str && *str != '\n')
	{
		*line = *str;
		line++;
		str++;
		i++;
	}
	return (line);
}

char	**str_to_tab(char* str)
{
	char	**tab;
	int		col;
	int		lin;
	int		i;


	i = 0;
	lin = lines(str);
	col = colones(str);
	tab = malloc(sizeof(char*) * (lin + 1));
	while (i < lin)
	{
		tab[i] = malloc(sizeof(char) * (col + 1));
		ft_strncpy(tab[i], str, col);
		str += col + 1;
		i++;
	}
	return (tab);
}

void	ft_puttab(char **tab)
{
	int		y;
	int		x;

	y = 0;
	while (tab[y])
	{
		x = 0;
		while (tab[y][x])
		{
			ft_putchar(tab[y][x]);
			x++;
		}
		ft_putchar('\n');
		y++;
	}
}

void	ist(int cont, int y, int x, char **map)
{
	if (map[y][x] == 'x')
	{
		map[y][x] = cont + '0';
		if (y > 0)
			ist(cont, y-1, x, map);
		ist(cont, y, x+1, map);
		if (x > 0)
			ist(cont, y, x-1, map);
		ist(cont, y+1, x, map);
		

	}
}

void	parc(char **map)
{
	int		y;
	int		x;
	int		cont;

	cont = 1;
	y = 0;
	while (map[y])
	{
		x = 0;
		while (map[y][x] && map[y][x] != '\n')
		{
			if (map[y][x] == 'x')
			{
				ist(cont, y, x, map);
				cont++;
			}
			x++;
		}
		y++;
	}
}

void	anal(char* file)
{
	int		fd;
	int		red;
	char	buf[BUFFER];
	char	**map;

	fd = open(file, O_RDONLY);
	red = read(fd, buf, BUFFER);
	buf[red] = '\0';
	map = str_to_tab(buf);
	ft_puttab(map);
	parc(map);
	ft_puttab(map);
	
}
