#ifndef __LETTRE_H__
# define __LETTRE_H__

# include "ft.h"
# include <unistd.h>
# include <stdlib.h>
# include <sys/types.h>
# include <sys/stat.h>
# include <fcntl.h>

# define BUFFER_SIZE	4096

int	conv(char *str);
char	*sort_letter(char *str);
int	can_i_write(char *word, char *rc);
void	file(char *rc, char *file);

#endif
