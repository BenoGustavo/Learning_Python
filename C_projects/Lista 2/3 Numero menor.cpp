//4 – Algoritmo 3 Menores Faça um algoritmo que leia 3 números inteiros e imprima o menor deles.

#include<conio.h>
#include<stdio.h>
#include<iostream>

//Variaveis

int N1,N2,N3;

//Inicio

main(){
	printf("Digite o primeiro numero: ");
	scanf("%i",&N1);
	
	printf("\nDigite o segundo numero: ");
	scanf("%i",&N2);
	
	printf("\nDigite o terceiro numero: ");
	scanf("%i",&N3);
	
	system("cls");
	
	if((N1<N2)&&(N1<N3)){
		printf("O menor numero eh %i",N1);
	}
	if((N2<N1)&&(N2<N3)){
	printf("O menor numero eh %i",N2);
	}
	if((N3<N1)&&(N3<N2)){
	printf("O menor numero eh %i",N3);
	}

	printf("\n\n");
	system("pause");
}
