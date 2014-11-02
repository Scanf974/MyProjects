#include "includes/ft.h"

int		main(void)
{
	t_list		*tool;

	tool = ft_create_elem('d');
	ft_list_push_front(&tool, 'e');
	ft_list_push_back(&tool, 'f');
	ft_putchar(tool->token);
	ft_putchar((tool->next)->token);
	ft_putchar((tool->next->next)->token);
	return (0);
}
