#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

char inicio,op;

main(){
	inicio:
		system("cls");
	
	int max = 123, low = 67;
	int rnd = 50 + (rand() % (50-100)); //Somar o valor minimo, pois assim o valor obtido sempre será maior que ele.
	
	printf("%i\n",rnd);
	
	printf("\nPressione qualquer tecla para retornar ou 'N' para sair.\n");
	op=getche();
	op=toupper(op);
	
	if(op=='N'){
		exit(0);
	}else{
		goto inicio;
	}
}
