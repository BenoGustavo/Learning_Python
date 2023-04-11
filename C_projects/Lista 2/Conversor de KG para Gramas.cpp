/*32. Faça um algoritmo que receba o peso de uma pessoa em quilos, calcule e mostre esse peso
em gramas.*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float kg,g;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Conversor de peso de KG para GRAMAS\n\n");
	printf("Insira o peso em KG: ");
	scanf("%f",&kg);
	
	g=kg*1000;
	
	system("cls");
	printf("Conversor de peso de KG para GRAMAS\n\n");
	printf("%.2fKG é igual à %.2fG",kg,g);
	
	printf("\n\n");
	system("pause");
}
