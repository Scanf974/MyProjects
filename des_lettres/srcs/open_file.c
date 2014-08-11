#include "../includes/lettre.h"

void	file(char *rc, char *file)
{
	int		fd;
	int		len;
	char	buf[1];
	char	word[50];

	len = 0;
	fd = open(file, O_RDONLY);
	while (read(fd, buf, 1))
	{
		if (buf[0] == '\n')
		{
			word[len] = '\0';
			if (len >= 7 && can_i_write(sort_letter(word), sort_letter(rc)))
			{
				if (len == 8)
					ft_putstr("\e[1;34m");
				else if (len == 9)
					ft_putstr("\e[1;32m");
				else if (len == 10)
					ft_putstr("\e[1;31m");
				else if (len >= 11)
					ft_putstr("\e[0;30m");
				else
					ft_putstr("\e[1;37m");

				ft_putstr(word);
				ft_putstr("\n");
			}
			read(fd, buf, 1);
			len = 0;
		}
		word[len] = buf[0];
		len++;
	}
	close(fd);
}
