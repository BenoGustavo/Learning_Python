/*27. Faça um algoritmo que receba dois números, calcule e mostre a divisão do primeiro
número pelo segundo. Sabe-se que o segundo número não pode ser zero, portanto não é
necessário se preocupar com validações.*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float num,div,res;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Calculadora de divisão entre dois números\n\n");
	printf("Insira o número que você deseja dividir: ");
	scanf("%f",&num);
	printf("Insira o divisor: ");
	scanf("%f",&div);
	
	res=num/div;
	
	system("cls");;
	printf("Calculadora de divisão entre dois números\n\n");
	printf("A sua divisão de %.2f por %.2f é igual à %.2f",num,div,res);
	
	printf("\n\n");
	system("pause");
}
