/*9. Leia um vetor de 40 posições e atribua valor 0 para todos os elementos que  possuírem valores negativos. */

//apresentar, - de 0 == 0

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

char inicio,op;
int q;

main(){
	setlocale(LC_ALL,"portuguese");
	
	inicio:
		system("cls");
	
	printf("Vetores - Exercicio 9\n\n");
	printf("Quantos indices você deseja? ");
	scanf("%i",&q);
	
	int vet[q];
	
	for (int i=0;i<q;i++){
		vet[i] = q - (rand() % (-q-q));
	}
	
	for (int i=0;i<q;i++){
		for (int j=0;j<q;j++){
			if(vet[i] == vet[j] && i != j){
				vet[i] = q - (rand() % (-q-q));
				j=j-1;
				i=i-1;
			}
		}
	}
	
	system("cls");
	printf("Vetores - Exercicio 9\n\n");
	
	printf("\nVetor original:\n\n");
	
	for(int i=0;i<q;i++){
		printf("Vetor [%i] = %i\n",i,vet[i]);
	}
	
	for(int i=0;i<q;i++){
		if(vet[i]<0){
			vet[i]=0;
		}
	}
	
	printf("\nVetor sem números negativos:\n\n");
	
	for(int i=0;i<q;i++){
		printf("Vetor [%i] = %i\n",i,vet[i]);
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
