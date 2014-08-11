CC = gcc
CFLAGS = -Wall -Wextra -Werror
EXEC = chiffres
LIB = -L. -lft

all: $(EXEC)

$(EXEC):
		$(CC) $(CFLAGS) main.c $(LIB) -o $(EXEC)

noflag:
		$(CC) main.c $(LIB) -o $(EXEC)
