/*36. Faça um algoritmo que receba o valor do salário mínimo e o valor do salário de um
funcionário, calcule e mostre a quantidade de salários mínimos que ganha esse funcionário.*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float salMin,salfunc,quantsal;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Divisor de salário por salário minimo\n\n");
	printf("Insira aqui o valor do salário minimo atual: ");
	scanf("%f",&salMin);
	printf("Insira aqui o valor do seu salário atual: ");
	scanf("%f",&salfunc);
	
	quantsal=salfunc/salMin;
	
	system("cls");
		printf("Divisor de salário por salário minimo\n\n");
		printf("Com o salário de %.2f, você recebe %.2f",salfunc,quantsal);
		
		
		printf("\n\n");
		system("pause");
}
