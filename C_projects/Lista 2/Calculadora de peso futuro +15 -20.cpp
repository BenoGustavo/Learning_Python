//*31. Faça um algoritmo que receba o peso de uma pessoa, calcule e mostre:
//a) o novo peso se a pessoa engordar 15% sobre o peso digitado;
//b) o novo peso se a pessoa emagrecer 20% sobre o peso digitado.
// + IMC PQ SIM

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

char Patualc[30],Pmais15c[30],Pmenos20c[30];
float Patual,P15,P20,Pmais15,Pmenos20;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Calculadora de peso futuro\n\n");
	printf("Insira aqui o seu peso atual em KG: ");
	scanf("%f",&Patual);
	
	P15=Patual*0.15; P20=Patual*0.20; Pmais15=Patual+P15 ; Pmenos20=Patual-P20;
	
	system("cls");
	
	printf("Calculadora de peso futuro\n\n");
	printf("Seu peso atual é %.2f, se você perder 20% (%.2f) de massa ficara com %.2f, se você ganhar 15% (%.2f) de massa ficara com %.2f",Patual,P20,Pmenos20,P15,Pmais15);
	
	printf("\n\n");
	system("pause");
}

