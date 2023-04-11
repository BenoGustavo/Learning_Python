/*05. Escreve um programa que sorteio, aleatoriamente, 10 números e 
armazene estes em um vetor.
Em seguida, o usuário digita um número e seu programa em C deve acusar 
se o número digitado está no vetor ou não. Se estiver, diga a posição que 
está*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

int vetor[9],selecao,achou=0;
char opcao;

main(){
	setlocale(LC_ALL,"portuguese");
	do{
		system("cls");
		srand(time(NULL));
	
	printf("Chute um valor de 0 a 100: ");
	scanf("%i",&selecao);
	
	for(int i=0;i<9;i++){
		vetor[i] = rand() % 100;
		printf("\nVetor[%i] = %i\n",i,vetor[i]);
	}
	
	for(int i=0;i<9;i++){

		if(vetor[i] == selecao){
			printf("\nParabéns, seu valor [%i] existe no indíce [%i]\n\n",selecao,i);
			achou++;
		}
	}
	
	if(achou == 0){
		printf("\n\nO valor que você digitou não foi encontrado\n\n");
	}
	
	printf("\n\nDeseja sair? (S) || (N)");
	opcao=getche();
	opcao=toupper(opcao);
	
	}while(opcao != 'S');
	
}
