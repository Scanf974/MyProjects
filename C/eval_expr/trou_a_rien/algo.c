while qu'il y a des jetons a lire:
	Lire le jeton
	if (jeton == nombre)
		ajouter a output queue
	if (jeton == o1) 						// o1 est l'operateur courant
		while (y a un autre o2 en haut de la stack && o1.priorite <= o2.priorite)
			pop o2 de la stack VERS output queue
		ajouter o1 sur la stack
	if (jeton == '(' )
		ajouter sur la stack
	if (jeton == ')' )
		while (jeton top de le stack != '(' )
			pop operateurs de la stack VERS output queue
		pop '(' de la stack VERS nul part					// je pense quon le supprime tout simplement
		if (stack epuise)
			...
	if (rien a lire)
		while (y des operateurs dans la stack)
			pop operateur dans output queue

