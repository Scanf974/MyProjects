#include "includes/ft.h"

t_list	*init_list(t_list *the_list)
{
	the_list = ft_create_elem('S');
	ft_remove_top(&the_list);
	return (the_list);
}

void	shunting_yard(t_list **line)
{
	t_list	*temp_line;
	t_list	*stack;
	t_list	*output_queue;

	temp_line = *line;
	output_queue = init_list(output_queue);
	stack = init_list(stack);
	while (temp_line)
	{
		if (temp_line->token >= '0' && temp_line->token <= '9')
			ft_list_push_front(&output_queue, temp_line->token);
		else
			ft_list_push_front(&stack, temp_line->token);
		temp_line = temp_line->next;
	}
	ft_putstr("LIN ");
	ft_print_list(line);
	ft_putstr("\nSTA ");
	ft_print_list(&stack);
	ft_putstr("\nOUT ");
	ft_print_list(&output_queue);
}
