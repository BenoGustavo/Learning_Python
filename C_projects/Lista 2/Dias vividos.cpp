/*Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de
vida ela possui. Considere sempre anos completos, e que um ano possui 365 dias. Ex: uma
pessoa com 19 anos possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ
VIVEU 6935 DIAS 5.*/

#include<conio.h>
#include<stdio.h> 
#include<iostream>
#include<locale.h>

int Anos,Dias;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Calculadora de dias vividos\n\n");
	printf("Digite aqui sua idade: \n");
	scanf("%i",&Anos);
	
	Dias = Anos * 365;
	system("cls");
	
	printf("Você viveu um total de %i anos, ou seja %i dias.",Anos,Dias);
	
	printf("\n\n");
	system("pause");
}
