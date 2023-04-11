//29. Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float valor,desconto,valorcd;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Desconto sobre um produto\n\n");
	printf("Insira aqui o valor do produto: ");
	scanf("%f",&valor);
	
	desconto=valor*0.1; valorcd=valor-desconto;
	
	system("cls");
	printf("Desconto sobre um produto\n\n");
	printf("O seu produto com valor de %.2fR$, com desconto fica 10% (%.2fR$) fica %.2fR$",valor,desconto,valorcd);
	
	printf("\n\n");
	system("pause");
}
