//14. Calcule a área de uma pizza que possui um raio R (pi=3.14).
//3.14*R^2

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

float raio,area;

main(){
	printf("Calculadora area do circulo\n\n");
	printf("Digite aqui o raio do seu circulo (Raio=Diamentro/2): ");
	scanf("%f",&raio);
	
	area = 3.14*pow(raio,2);
	
	system("cls");
	printf("Calculadora area do circulo\n\n");
	
	printf("O seu cirulo com raio de %.2f, tem a area de %.2f",raio,area);
	
	printf("\n\n");;
	system("pause");
}
