//25. Calcule o volume de uma caixa de água cilíndrica.

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float raio,area,altura,volume;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Calculadora de volume caixa de água CILÍNDRICA\n\n");
	printf("Insira aqui o raio da caixa de água (Raio=Diametro/2) em cm: ");
	scanf("%f",&raio);
	printf("Insira aqui a altura da caixa de água em cm: ");
	scanf("%f",&altura);
	
	area=(3.14*(pow(raio,2)));
	
	volume=area*altura;
	
	volume=volume/1000;
	area=area/1000;
	
	system("cls");
	
	printf("Calculadora de volume caixa de água CILÍNDRICA\n\n");
	printf("A área da sua caixa dÁgua é %.2f metros quadrados, e tem %.2f metros quadrados de volume",area,volume);
	
	printf("\n\n");
	system("pause");
}
