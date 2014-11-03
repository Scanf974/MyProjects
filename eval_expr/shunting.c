#include "includes/ft.h"

t_list	*init_list(t_list *the_list)
{
	the_list = ft_create_elem('S');
	ft_remove_top(&the_list);
	return (the_list);
}

int		is_ope(char token)
{
	if (token == '+' || token == '-')
		return (2);
	else if (token == '*' || token == '/')
		return (3);
	return (0);
}

void	shunting_yard(t_list **line)
{
	t_list	*temp_line;
	t_list	*stack;
	t_list	*output_queue;

	temp_line = *line;

	ft_putstr("LIN ");
	ft_print_list(line);
	ft_putchar('\n');

	output_queue = init_list(output_queue);
	stack = init_list(stack);
	while (temp_line)
	{
		ft_putstr("\nla on entre ");
		if (temp_line->token >= '0' && temp_line->token <= '9')
			ft_list_push_front(&output_queue, temp_line->token);
		else if (is_ope(temp_line->token))
		{
			if (stack)
			{
				ft_putstr("Ya un ope\n");
				while (stack && is_ope(temp_line->token) <= is_ope(stack->token))
				{
					ft_list_push_front(&output_queue, stack->token);
					ft_remove_top(&stack);
				}
			}
			ft_list_push_front(&stack, temp_line->token);
		}
		else
		{
			ft_putstr("mais que cest il passer\n");
			ft_list_push_front(&stack, temp_line->token);
		}

		ft_putstr("STA ");
		ft_print_list(&stack);
		ft_putstr("\nOUT ");
		ft_print_list(&output_queue);
		ft_putchar('\n');
		temp_line = temp_line->next;
	}
}
