/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: exam <marvin@42.fr>                        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2015/03/11 11:27:24 by exam              #+#    #+#             */
/*   Updated: 2015/03/11 11:28:13 by exam             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "hh.h"

void	ft_putstr(char *str)
{
	while (*str)
		write(1, str++, 1);
}
