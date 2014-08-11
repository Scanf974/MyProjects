#include <stdio.h>
#include <string.h>
	
void swap(char* chaine,int ind1,int ind2)
{
	char tmp = chaine[ind1];
	chaine[ind1] = chaine[ind2];
	chaine[ind2] = tmp;

}
	
void Test(char* chaine,int taille,int curs)
{
	int i;
	if (taille-curs<=1)
		printf("%s\n",chaine);
	else
	{
		for(i=curs;i<taille;i++)
		{
			swap(chaine,i,curs);
			Test(chaine,taille,curs+1);
			swap(chaine,i,curs);
		}
	}
}

int main(void)
{
	char cp[] = "ABC";

	Test(cp,strlen(cp),0);
	return 0;
}
