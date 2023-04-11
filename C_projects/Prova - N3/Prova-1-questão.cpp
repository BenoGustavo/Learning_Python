/* Prova EX.1 */

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<time.h>

char sair;
int vetor[13],indice1,indice2,multi;

main(){
	setlocale(LC_ALL,"portuguese");
	do{
		system("cls");
		printf("Exercicio 1 - PROVA\n\n");
		srand(time(NULL));
		
		for(int i=0;i<13;i++){
			vetor[i] = rand() % 201;
		}
		
		//verificar repetição dentro do codigo
		
		for(int i=0; i<13; i++){
        	for(int a=0; a<13; a++){
    			if(i == a)
        		continue;
        			if(vetor[i] == vetor[i])
        			vetor[a] = rand()%201;
        	}
   		}
		
		//mostrar vetor dentro do codigo
		
		for(int i=0;i<13;i++){
			printf("\nVetor[%i] = %i\n",i,vetor[i]);
		}
		
		system("cls");
		
		do{
			
		for(int i=0;i<13;i++){
			printf("\nVetor[%i] = %i\n",i,vetor[i]);
		}
		
		printf("\nInsira o indice desejado: ");
		scanf("%i",&indice1);
		
		printf("\nInsira o indice desejado: ");
		scanf("%i",&indice2);
		
		if(indice1 > 13 || indice2 > 13 || indice1 < 0 || indice2 < 0){
			system("cls");
			printf("Exercicio 1 - PROVA\n\n");
			printf("Por favor, insira um valor valido\n\n");
			system("pause");
			system("cls");
		}
	}while(indice1 > 13 || indice2 > 13 || indice1 < 0 || indice2 < 0);
		
		system("cls");
		
		printf("Exercicio 1 - PROVA\n\n");
		printf("O primeiro indice desejado é (%i): vetor(%i) = %i\n",indice1,indice1,vetor[indice1]);
		printf("O segundo indice desejado é (%i): vetor(%i) = %i",indice2,indice2,vetor[indice2]);
		
		multi = vetor[indice1] * vetor[indice2];
		
		printf("\n\nE a multiplicação entre ambos é (%i)",multi);
		
		printf("\n\nAperte qualquer tecla para retornar ou 'N' para sair\n\n");
		sair=getche();
		sair=toupper(sair);
		
	}while(sair != 'N');
	
	printf("Saindo...");
}
