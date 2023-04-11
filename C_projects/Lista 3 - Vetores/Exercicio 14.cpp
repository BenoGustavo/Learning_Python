/*14. Leia 3 vetores de 9 posições e crie outro com o 1º terço do primeiro, o  segundo 3º. do segundo e o último terço do 3º. Escrever o vetor resultante ao  final. */

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

int vetA[8],vetB[8],vetC[8],vetD[8];
char inicio,slc,op;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Vetores - Exercicio 14\n\n");
	
	inicio:
		system("cls");
	
	printf("Menu:\n");
	printf("1 - Inserir os valores manualmente\n");
	printf("2 - Aleatorizar os valores\n");
	slc=getche();
	
	switch(slc){
		case '1':{
			system("cls");
			printf("Vetores - Exercicio 14\n\n");
			
			printf("\n\nInicio do vetor A\n\n");
			
			for(int i=0;i<9;i++){
				printf("\nInsira o valor do vetor A [%i]: ",i);
				scanf("%i",&vetA[i]);
			}
			
			printf("\n\nInicio do vetor B\n\n");
			
			for(int i=0;i<9;i++){
				printf("\nInsira o valor do vetor B [%i]: ",i);
				scanf("%i",&vetB[i]);
			}
			
			printf("\n\nInicio do vetor C\n\n");
			
			for(int i=0;i<9;i++){
				printf("\nInsira o valor do vetor C [%i]: ",i);
				scanf("%i",&vetC[i]);
			}
			
			break;
		}
		case '2':{
			
			for(int i=0;i<9;i++){
				vetA[i] = rand() % 101 ;vetB[i] = rand() % 101 ;vetC[i] = rand() % 101;
			}
			
				for (int i=0;i<9;i++){
				for (int j=0;j<9;j++){
				if(vetA[i] == vetA[j] && i != j){
				vetA[i] = rand() % 101;
				j=j-1;
				i=i-1;
			}
		}
	}
	
			for (int i=0;i<9;i++){
			for (int j=0;j<9;j++){
			if(vetB[i] == vetB[j] && i != j){
				vetB[i] = rand() % 101;
				j=j-1;
				i=i-1;
			}
		}
	}
	
		for (int i=0;i<9;i++){
		for (int j=0;j<9;j++){
			if(vetC[i] == vetC[j] && i != j){
				vetC[i] = rand() % 101;
				j=j-1;
				i=i-1;
			}
		}
	}
			
			break;
		}
		
		default:{
			goto inicio;
			break;
		}
	}
	
	system("cls");
	printf("Vetores - Exercicio 14\n\n");
	
	//1º terço do primeiro
	
	for(int i=0;i<3;i++){
		vetD[i] = vetA[i];
	}
	
	//o  segundo 3º. do segundo
	
		for(int i=3;i<7;i++){
		vetD[i] = vetB[i];
	}
	
	//último terço do 3º.
	
		for(int i=6;i<9;i++){
		vetD[i] = vetC[i];
	}
	
	// TELA
	
	printf("Vetor A:\n\n");
	
	for(int i=0;i<9;i++){
		printf("Vetor A[%i] = %i\n",i,vetA[i]);
	}
	
	printf("\nVetor B:\n\n");
	
	for(int i=0;i<9;i++){
		printf("Vetor B[%i] = %i\n",i,vetB[i]);
	}
	
	printf("\nVetor A:\n\n");
	
	for(int i=0;i<9;i++){
		printf("Vetor C[%i] = %i\n",i,vetC[i]);
	}
	
	printf("\nVetor resultante:\n\n");
	for(int i=0;i<9;i++){
		printf("Vetor D[%i] = %i\n",i,vetD[i]);
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
