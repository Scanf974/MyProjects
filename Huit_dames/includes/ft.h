#ifndef __FT_H__
# define __FT_H__

# include <unistd.h>

# define UPCASE(x) (x >= 'A' && x <= 'Z')
# define LOWCASE(x) (x >= 'a' && x <= 'z')

void	ft_putchar(char c);
void	ft_putstr(char *str);
void	ft_putnbr(int number);
int		ft_strlen(char *str);
char    *ft_strcpy(char *dest, char *src);
char    *ft_strncpy(char *dest, char *src, unsigned int n);
char	*ft_strstr(char *str, char *to_find);
int		ft_strcmp(char *s1, char *s2);
int		ft_strncmp(char *s1, char *s2, unsigned int n);
char	*ft_strupcase(char *str);
char	*ft_strlowcase(char *str);

#endif
