/*18. A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora
extra. Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um
determinado funcionário. Considere que o salário líquido é igual ao salário bruto descontando-
se 10% de impostos.*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float horastrabalhadas,horasEXTRAStrabalhadas,dindinhora,dindinextra,dindintotal,salarioliq,desconto;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Calculadora de horas e horas extras trabalhadas\n\n");
	printf("Digite aqui a quantidade de horas trabalhadas: ");
	scanf("%f",&horastrabalhadas);
	
	printf("Digite aqui a quantidade de horas EXTRAS trabalhadas: ");
	scanf("%f",&horasEXTRAStrabalhadas);
	
	dindinhora = horastrabalhadas * 10;
	dindinextra = horasEXTRAStrabalhadas * 15;
	
	dindintotal = dindinhora + dindinextra;
	
	desconto = dindintotal*0.1;
	
	salarioliq = dindintotal - desconto;
	
	//printf("%.2f, %.2f, %.2f",salarioliq,dindintotal,desconto);
	
	//system("pause");
	
	system("cls");
	printf("Calculadora de horas e horas extras trabalhadas\n\n");
	
	
	printf("Voce tem %.0f horas trabalhadas, e %.0f horas extras\n",horastrabalhadas,horasEXTRAStrabalhadas);
	printf("O seu salario liquido é de: %.2f\nO seu salario bruto é de: %.2f",salarioliq,dindintotal);
	
	
	printf("\n\n");
	system("pause");
}
