#include "includes/ft.h"

t_list	*ft_create_elem(char token)
{
	t_list	*new_element;
	
	new_element = malloc(sizeof(t_list));
	new_element->token = token;
	new_element->next = NULL;
	return (new_element);
}

void	ft_list_push_front(t_list **begin_list, char token)
{
	t_list	*new_element;

	new_element = ft_create_elem(token);
	new_element->next = *begin_list;
	*begin_list = new_element;
}

void	ft_list_push_back(t_list **begin_list, char token)
{
	t_list	*new_element;
	t_list	*curent_list;

	new_element = ft_create_elem(token);
	curent_list = *begin_list;
	while (curent_list->next)
		curent_list = curent_list->next;
	curent_list->next = new_element;
}

void	ft_remove_top(t_list **begin_list)
{
	t_list	*temp;
	
	// Ca ne sert pas encore a grand chose, psk ya pas de free
	temp = *begin_list;
	temp = temp->next;
	*begin_list = temp;
}
