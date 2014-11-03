#ifndef __ft_list_h__
# define __ft_list_h__

typedef struct		s_list
{
	struct s_list	*next;
	char			token;
}					t_list;

t_list	*ft_create_elem(char token);
void	ft_list_push_front(t_list **begin_list, char token);
void	ft_list_push_back(t_list **begin_list, char token);
void	ft_remove_top(t_list **begin_list);
void	ft_print_list(t_list **begin_list);

#endif

