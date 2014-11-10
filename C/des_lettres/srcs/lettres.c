#include "../includes/lettre.h"

int		can_i_write(char *word, char *rc)
{
	int		i;
	int		j;

	i = 0;
	j = 0;
	while (rc[i] && word[j])
	{
		if (word[j] == rc[i])
			j++;
		i++;
	}
	if (!word[j])
		return (1);
	return (0);
}
