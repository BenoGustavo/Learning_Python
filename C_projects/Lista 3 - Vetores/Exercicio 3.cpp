/*

3 - Escreva um programa que leia 733 números aleatórios de 0 até 300 e
imprima o maior deles e quantas vezes o maior número foi lido, apresentando
este e suas respectivas posições.

*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

char inicio;
int vet[732],maior,rep=0,op;

main(){
	inicio:
		rep=0;
		system("cls");
		
	int indice[rep];
	
	setlocale(LC_ALL,"portuguese");
	printf("Vetores exercicio 3\n\n");
	
	printf("Vetores\n");
	
	for(int i=0;i<732;i++){
		vet[i] = rand() % 301;
		printf("Vet[%i] = %i\n",i,vet[i]);
	}
	
	maior = 0;
	
	for(int i=0;i<732;i++){
		if(vet [i] >= maior){
				maior = vet[i];
			}
	}
	
	for(int i=0;i<732;i++){
		if(vet[i] == maior){
			indice[rep] = i;
			rep = rep+1;
		}
	}
	
	printf("\nO maior valor é: %i\n",maior);
	printf("Aparece nos indices: ");
	for(int i=0;i<rep;i++){
		printf("%i ",indice[i]);
	}
	
	printf("\n\nAperte qualquer tecla para fazer novamente ou [N] para sair\n");
	op=getche();
	op=toupper(op);
	
	switch(op){
		case 'N':{
			printf("\n\n");
			printf("Saindo...\n");
			exit(0);
			break;
		}
		default:{
			goto inicio;
			break;
		}
	}
	
	printf("\n\n");
	system("pause");
}
