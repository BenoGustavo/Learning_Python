/*17. Alguns países medem temperaturas em graus Celsius, e outros em graus Fahrenheit. Faça
um algoritmo para ler uma temperatura Celsius e imprimi-la em Fahrenheit (pesquise como
fazer este tipo de conversão).*/

//Formula: Fahrenheit = Celsius * 1,8 +32

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

float Celsius,Fahrenheit;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Conversor Celsius para Fahrenheit\n\n");
	printf("Insira aqui a temperatura em celsius: ");
	scanf("%f",&Celsius);
	
	Fahrenheit = Celsius * 1.8 + 32;
	
	system("cls");
	
	printf("Conversor Celsius para Fahrenheit\n\n");
	printf("A temperatura %.2fº em Celsius é igual à %.2fº Fahrenheit.",Celsius,Fahrenheit);
	
	printf("\n\n");
	system("pause");
}
