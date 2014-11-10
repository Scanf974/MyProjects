#include "includes/ft.h"

int		main(int argc, char *argv[])
{
	int		i;
	t_list	*line;

	i = 0;
	if (argc >= 2)
	{
		while (argv[1][i])
		{
			if(argv[1][i] != ' ')
				ft_list_push_back(&line, argv[1][i]);
			i++;
		}
		shunting_yard(&line);
	}
	return (0);
}
