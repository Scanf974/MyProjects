/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: exam <marvin@42.fr>                        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2015/03/11 11:07:08 by exam              #+#    #+#             */
/*   Updated: 2015/03/11 11:39:45 by exam             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "hh.h"

int		ft_strcmp(char *s1, char *s2)
{
	int		i;
	char	c1;
	char	c2;

	i = 0;
	while (s1[i])
	{
		c1 = s1[i];
		c2 = s2[i];
		if (s1[i] >= 'A' && s1[i] <= 'Z')
			c1 += 32;
		if (s2[i] >= 'A' && s2[i] <= 'Z')
			c2 += 32;
		if (c1 != c2)
			return (c1 - c2);
		i++;
	}
	c2 = s2[i];
	if (s2[i] >= 'A' && s2[i] <= 'Z')
		c2 += 32;
	if (s2[i])
		return (s1[i] - c2);
	return (0);
}

void	ft_swap(char **s1, char **s2)
{
	char	*save;

	save = ft_strdup(*s1);
	*s1 = ft_strdup(*s2);
	*s2 = ft_strdup(save);
}

void	ft_printtab(char **tab)
{
	int		i;
	int		len;

	i = 0;
	while (tab[i])
	{
		len = ft_strlen(tab[i]);
		ft_putstr(tab[i]);
		i++;
		if (tab[i] && len != ft_strlen(tab[i]))
			ft_putchar('\n');
		else if (tab[i])
			ft_putchar(' ');
	}
}

void	ft_ord(char **av)
{
	int		i;
	int		j;
	int		res;

	i = 0;
	while (av[i])
	{
		j = i + 1;
		while (av[j])
		{
			if (ft_strlen(av[i]) > ft_strlen(av[j]))
				ft_swap(&av[i], &av[j]);
			j++;
		}
		i++;
	}
	i = 0;
	while (av[i])
	{
		j = i + 1;
		while (av[j])
		{
			res = ft_strcmp(av[i], av[j]);
			if (res > 0 && ft_strlen(av[i]) == ft_strlen(av[j]))
				ft_swap(&av[i], &av[j]);
			j++;
		}
		i++;
	}
}

int		main(int ac, char **av)
{
	char	**tab;

	if (ac == 2)
	{
		tab = ft_strsplit(av[1]);
		ft_ord(tab);
		ft_printtab(tab);
	}
	write(1, "\n", 1);
	return (0);
}
