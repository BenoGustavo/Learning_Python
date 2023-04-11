/*30. Um funcionário recebe um salário fixo
mais 4% de comissão sobre as vendas. Faça um algoritmo que receba o salário fixo de um
funcionário e o valor de suas vendas, calcule e mostre a comissão e o salário final do
funcionário.*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float salario,vendas,comissao,salfinal;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Calculadora de salário comissão\n\n");
	printf("Insira aqui o salário: ");
	scanf("%f",&salario);
	printf("Insira aqui o valor feito em vendas: ");
	scanf("%f",&vendas);
	
	comissao=vendas*0.04; salfinal=comissao+salario;
	
	system("cls");
	printf("Calculadora de salário comissão\n\n");
	printf("O você recebeu %.2f de comissão, seu salário final é de %.2f",comissao,salfinal);
	
	printf("\n\n");
	system("pause");
	
}
