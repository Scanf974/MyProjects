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

t_list	*ft_list_reverse(t_list **begin_list)
{
	t_list	*temp;
	t_list	*rev;

	temp = *begin_list;
	rev = init_list(rev);
	while (temp)
	{
		ft_list_push_front(&rev, temp->token);
		temp = temp->next;
	}
	return (rev);
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
		else if (is_ope(temp_line->token))
		{
			if (stack)
			{
				while (stack && is_ope(temp_line->token) <= is_ope(stack->token))
				{
					ft_list_push_front(&output_queue, stack->token);
					ft_remove_top(&stack);
				}
			}
			ft_list_push_front(&stack, temp_line->token);
		}
		else if (temp_line->token == '(')
			ft_list_push_front(&stack, temp_line->token);
		else if (temp_line->token == ')')
		{
			while (stack->token != '(')
			{
				ft_list_push_front(&output_queue, stack->token);
				ft_remove_top(&stack);
			}
			ft_remove_top(&stack);
		}
		temp_line = temp_line->next;
	}
	while (stack)
	{
		ft_list_push_front(&output_queue, stack->token);
		ft_remove_top(&stack);
	}
	output_queue = ft_list_reverse(&output_queue);
	ft_print_list(&output_queue);
}
