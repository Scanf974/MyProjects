/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strplit.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: exam <marvin@42.fr>                        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2015/03/11 11:06:52 by exam              #+#    #+#             */
/*   Updated: 2015/03/11 11:30:11 by exam             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "hh.h"

int		ft_nb_words(char *str)
{
	int		i;
	int		nb;

	i = 0;
	nb = 0;
	while (str[i])
	{
		if (str[i] != ' ' && str[i + 1] == ' ')
			nb++;
		i++;
	}
	return (nb + 1);
}

int		ft_strlen_spec(char *str)
{
	int		i;

	i = 0;
	while (str[i] && str[i] > ' ')
		i++;
	return (i);
}

char	*ft_strdup_spec(char *str)
{
	char	*dst;
	int		i;

	dst = (char *)malloc(sizeof(char) * (ft_strlen_spec(str) + 1));
	i = 0;
	while (str[i] && str[i] > ' ')
	{
		dst[i] = str[i];
		i++;
	}
	dst[i] = 0;
	return (dst);
}

char	**ft_strsplit(char *str)
{
	char	**tab;
	int		nb_w;
	int		i;

	nb_w = ft_nb_words(str);
	tab = (char **)malloc(sizeof(char *) * (nb_w + 1));
	i = 0;
	while (i < nb_w)
	{
		while (*str <= ' ')
			str++;
		tab[i] = ft_strdup_spec(str);
		str += ft_strlen_spec(str) + 1;
		i++;
	}
	tab[i] = 0;
	return (tab);
}
