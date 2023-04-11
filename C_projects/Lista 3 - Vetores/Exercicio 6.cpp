//6. Leia um vetor de 16 posições e troque os 8 primeiros valores pelos 8 últimos e vice-e-versa. Escreva ao final o vetor obtido.

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

int vet[15];
char op,inicio,menu,aaa;

main(){
	menu:
	
	setlocale(LC_ALL,"portuguese");
	do{
		system("cls");
	
	printf("Vetores - Exercicio 6\n\n");
	printf("Escolha:\n");
	printf("1 - Inserir os valores manualmente\n");
	printf("2 - Aleatorizar o vetor\n");
	printf("3 - Sair");
	op=getche();
	
	if(op>'3'){
		printf("\n\nValor invalido...\nRetornando.\n\n");
		system("pause");
	}
}while(op>'3');
	
	switch(op){
		case '1':{
			system("cls");
			printf("Vetores - Exercicio 6\n");
			for(int i=0;i<16;i++){
				printf("\nInsira o [%i] vetor: ",i);
				scanf("%i",&vet[i]);
			}
			
			goto inicio;
			
			break;
		}
		case '2':{
			system("cls");
			printf("Vetores - Exercicio 6\n\n");
			
			for(int i=0;i<16;i++){
			vet[i] = rand() % 1000;
			}
			
			//Não repetir números
			
			for(int i=0; i<16; i++){
         		for(int a=0; a<16; a++){
             	if(i == a)
                 continue;
             	if(vet[i] == vet[i])
                 	vet[a] = rand()%1000;
        		}
     		}
     		
     		for(int i=0;i<16;i++){
			printf("Vet[%i] = %i\n",i,vet[i]);
			}
			
			goto inicio;
			
			break;
		}
		case '3':{
			system("cls");
			printf("Vetores - Exercicio 6\n\n");
			printf("Saindo...\n\n");
			system("pause");
			exit(0);
			
			break;
		}
	}
	
	inicio:
		
	int vetInvertido[15];
	
	for(int i=0;i<16;i++){
		if(i<8){
			vetInvertido[i+8] = vet[i];
		}
		
		if(i>=8 && i<= 16){
			vetInvertido[i-8] = vet[i];
		}
	}
	
	for(int i=0;i<16;i++){
		printf("\nVetor %i - [%i]",i,vet[i]);
	}
	
	printf("\n\nVetores Invertidos\n\n");
	
	for(int i=0;i<16;i++){
		
		printf("Vetor invertido [%i] = %i\n",i,vetInvertido[i]);
	}
	
	printf("\n\n Aperte qualquer botão para retornar ou 'N' para sair.\n");
	aaa=getche();
	aaa=toupper(aaa);
	
	switch(aaa){
		case 'N':{
			system("cls");
			printf("\nSaindo...\n");
			system("pause");
			exit(0);
			break;
		}
		default:{
			goto menu;
			break;
		}
	}
	
	system("pause");
	
}
