/* Prova EX.2 */

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

char sair,menu,inicio,middle;
float vetorA[4],vetorB[4];

main(){
	setlocale(LC_ALL,"portuguese");
	
	inicio:
	
	do{
		system("cls");
		
		do{
		
		printf("Exercicio - PROVA QUESTÃO 2\n\n");
		printf("Menu:\n");
		printf("1 - Aleatorizar os vetores\n");
		printf("2 - Inserir manualmente\n");
		menu = getche();
		
			if(menu>'2' || menu< '1'){
				system("cls");
				printf("Exercicio 2 - PROVA\n\n");
				printf("Por favor, insira um valor valido\n\n");
				system("pause");
				system("cls");
			}
			
		}while(menu > '2' || menu < '1');
		
		system("cls");
		
		switch(menu){
			case '1':{
			
				for(int i=0;i<5;i++){
					vetorA[i] =  rand() % 201;
					vetorB[i] =  rand() % 201;
				}
				
				//verificar repetição dentro do codigo
		
				for(int i=0; i<5; i++){
        			for(int a=0; a<5; a++){
    					if(i == a)
        					continue;
        						if(vetorA[i] == vetorA[i])
        							vetorA[a] = rand()%201;
        			}
   				}
   				
   				for(int i=0; i<5; i++){
        			for(int a=0; a<5; a++){
    					if(i == a)
        					continue;
        						if(vetorB[i] == vetorB[i])
        							vetorB[a] = rand()%201;
        			}
   				}
   				
   				for(int i=0;i<5;i++){
   					printf("\nVetorA(%i) = %.2f , VetorB(%i) = %.2f",i,vetorA[i],i,vetorB[i]);
				   }
				   
				   printf("\n\n");
				   system("pause");
				
				break;
			}
			
			case '2':{
				for(int i=0;i<5;i++){
					printf("\nInsira o valor do indice (%i) do VetorA: ",i);
					scanf("%f",&vetorA[i]);
				}
				
				for(int i=0;i<5;i++){
					printf("\nInsira o valor do indice (%i) do VetorB: ",i);
					scanf("%f",&vetorB[i]);
				}
				
				system("cls");
				
				for(int i=0;i<5;i++){
   					printf("\nVetorA(%i) = %.2f , VetorB(%i) = %.2f",i,vetorA[i],i,vetorB[i]);
				}
				
				printf("\n\n");
				system("pause");
				
				break;
			}
		}
		
		middle:
		
		system("cls");
		
		printf("Exercicio - PROVA QUESTÃO 2\n\n");
		printf("Menu:\n");
		printf("1 - Soma dos vetores indice a indice\n");
		printf("2 - Localizar maior no vetorA e menor no vetorB\n");
		printf("3 - Ler novos valores\n");
		printf("4 - Sair\n");
		menu = getche();
		
		switch(menu){
			case '1':{
				float soma[4];
				
				system("cls");
				printf("Exercicio - PROVA QUESTÃO 2\n\n");
				
				for(int i=0;i<5;i++){
					soma[i] = vetorA[i] + vetorB[i];
				}
				
				for(int i=0;i<5;i++){
   					printf("\nVetorA(%i) = %.2f , VetorB(%i) = %.2f , VetorSoma(%i) = %.2f",i,vetorA[i],i,vetorB[i],i,soma[i]);
				}
				
				break;
			}
			
			case '2':{
				system("cls");
				fflush(stdin);
				
				int indiceA,indiceB;
				float menor = vetorA[0],maior = vetorB[0];
				
				printf("Exercicio - PROVA QUESTÃO 2\n\n");
				
				for(int i=0;i<5;i++){
					
					if(vetorA[i] < menor){
						menor = vetorA[i];
						
						indiceA = i;
						
					}
				}
				
				for(int i=0;i<5;i++){
					
					if(vetorB[i] > maior){
						maior = vetorB[i];
						
						indiceB = i;
					}
				}
				
				for(int i=0;i<5;i++){
   					printf("\nVetorA(%i) = %.2f , VetorB(%i) = %.2f",i,vetorA[i],i,vetorB[i]);
				}
				
				printf("\n\nO Vetor A no indice (%i) tem o menor valor alocado %.2f\n",indiceA,menor);
				printf("\nO Vetor B no indice (%i) tem o maior valor alocado %.2f\n",indiceB,maior);
				
				break;
			}
			
			case '3':{
				system("cls");
				
				goto inicio;
				
			}
			
			case '4':{
				system("cls");
				exit(0);
				
				break;
			}
		}
		
		printf("\n\nAperte qualquer tecla para ler novos valores ou 'S' para retornar ao menu\n\n");
		sair=getche();
		sair=toupper(sair);
		
		if(sair == 'S'){
			goto middle;
		}
		
	}while(sair != 'S');
}
