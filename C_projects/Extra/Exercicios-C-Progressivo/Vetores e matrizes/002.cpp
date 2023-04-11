/*01. Crie um programa em C que peça 10 números, armazene eles em um 
vetor e diga qual elemento é o menor, e seu valor.
*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

int vetor[9],menor=0,maior=0;
char opcao;

main(void){
	do{
		menor=0; maior=0;
		system("cls");
		
	setlocale(LC_ALL,"portuguese");
	srand(time(NULL));
	
	for(int i=0;i<10;i++){
		vetor[i] = rand() % 100;
	}
	
	for(int i=0; i<10; i++){
    for(int a=0; a<10; a++){
    if(i == a)
    continue;
    if(vetor[i] == vetor[i])
    vetor[a] = (rand() % (100));
       	}
   	}
	
	for(int i=0;i<10;i++){
		
		printf("Vetor[%i] = %i\n",i,vetor[i]);
		if(vetor[i] < menor){
			menor = vetor[i];
		}
		
		if(vetor[i] > maior){
			maior = vetor[i];
		}
	}
	
	printf("\n");
	
	for(int i=0;i<10;i++){
		if(vetor[i] == menor){
			printf("O menor elemento é [%i]\n",vetor[i]);
			i = 11;
		}
	}
	
	for(int i=0;i<10;i++){
		if(vetor[i] == maior){
			printf("O maior elemento é [%i]\n",vetor[i]);
			i = 11;
		}
	}
	
	printf("\n\nDeseja sair? (S) || (N)");
	opcao=getche();
	opcao=toupper(opcao);
	
	}while(opcao != 'S');
}
