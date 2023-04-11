/* 20. Uma confecção produz X blusas de lã e para isto gasta uma certa quantidade de novelos.
Faça um algoritmo para calcular quantos novelos de lã ela gasta por blusa. */

//cada blusa gasta 3 novelos de lã

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

int camisas,la,totalla;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Calculadora de blusas X novelo de lã\n\n");
	printf("Digite a quantidade de camisas a serem feitas: ");
	scanf("%i",&camisas);
	
	la =3;
	
	totalla = camisas*la;
	
	system("cls");
	printf("Para realizar a confecção de %i blusas é necessário %i lã",camisas,totalla);
	
	printf("\n\n");
	system("pause");
}
