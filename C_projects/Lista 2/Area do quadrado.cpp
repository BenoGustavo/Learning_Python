//34. Faça um algoritmo que calcule e mostre a área de um quadrado. Sabe-se que: A = lado * lado

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float lado,a;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Area do quadrado\n\n");
	printf("Insira aqui o valor de qualquer lado do quadrado: ");
	scanf("%f",&lado);
	
	a=lado*lado;
	
	system("cls");
	
	printf("Area do quadrado\n\n");
	printf("A area de quadrado de lado %.2f é igual à %.2f",lado,a);
		
		printf("\n\n");
		system("pause");
}
