/*5. Declare um vetor de 10 posições e o preencha com os 10 primeiros
números impares e o escreva.*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

char op,inicio;
int vet[9],vetimp[9];

main(){
	setlocale(LC_ALL,"portuguese");
	
	inicio:
	
	srand (time(NULL));
	system("cls");
	printf("Vetores - Exercicio 5\n\n");
	
	for(int i=0;i<10;){
		vet[i] = rand() % 1001;
		if(vet[i] % 2 != 0){
			vetimp[i]=vet[i];
			i++;
		}
	}
	
	system("cls");
	printf("Vetores - Exercicio 5\n\n");
	printf("Os 10 primeiros números impares gerados foram:\n");
	for(int i=0;i<10;i++){
		printf("Vetor Impar[%i] = %i\n",i,vetimp[i]);
	}
	printf("\nPressione qualquer tecla para retornar ou 'N' para sair.\n");
	op=getche();
	op=toupper(op);
	
	if(op=='N'){
		exit(0);
	}else{
		goto inicio;
	}
	
}
