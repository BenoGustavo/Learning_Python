/*2. Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os
cavalos comprados para um haras.*/

#include<conio.h>
#include<stdio.h> 
#include<iostream>
#include<locale.h>

int NdeCavalos,NdeFerraduras;

main(){
	
setlocale(LC_ALL,"portuguese");
	printf("Contador de ferradura para cavalos\n\n");
	printf("Digite aqui o número de cavalos aos quais você quer colocar uma ferradura: ");
	scanf("%i",&NdeCavalos);
	
	NdeFerraduras = NdeCavalos * 4;
	
	system("cls");
	
	printf("O número de ferraduras necessarias é %i",NdeFerraduras);
	
	printf("\n\n");
	system("pause");	
}


