#include "../includes/lettre.h"

char	*ft_strcpy(char *dest, char *src)
{
	int		i;

	i = 0;
	while (src[i])
	{
		dest[i] = src[i];
		i++;
	}
	dest[i] = '\0';
	return (dest);
}

int		ft_strlen(char *str)
{
	int		len;

	len = 0;
	while (str[len] && str[len] != '\n')
		len++;
	return (len);

}

char	*sort_letter(char *str)
{
	int		i;
	int		j;
	char	save_cac;
	char	*new;

	i = 0;
	new = malloc(sizeof(char) * (ft_strlen(str) + 1));
	ft_strcpy(new, str);
	while (new[i])
	{
		j = i + 1;
		while (new[j])
	{
			if (new[j] < new[i])
			{
				save_cac = new[j];
				new[j] = new[i];
				new[i] = save_cac;
			}
			j++;
		}
		i++;
	}
	return (new);
}
