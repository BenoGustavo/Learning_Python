/*1. A imobiliária Imóbilis vende apenas terrenos retangulares. Faça um algoritmo para ler as
dimensões de um terreno e depois exibir a área do terreno.

bibliotecas*/

#include<stdio.h>
#include<iostream>
#include<conio.h>
#include<locale.h>

float AlturaDoTerreno,LarguraDoTerreno,AreaTotal;


main(){
setlocale(LC_ALL,"portuguese");
	printf("Imobiliaria Imóbilis, Seja bem vindo\n\n");
	printf("Digite a altura do terreno.\n:");
	scanf("%f",&AlturaDoTerreno);
	
	printf("\nDigite a largura do terreno.\n:");
	scanf("%f",&LarguraDoTerreno);
	
	system("cls");
	
	AreaTotal = AlturaDoTerreno * LarguraDoTerreno;
	
	printf("Seu terreno tem %.2f de altura, %.2f de largura, e %.2f metros quadrados.",AlturaDoTerreno,LarguraDoTerreno,AreaTotal);
	
	
	printf("\n\n");
	system("pause");
}

