/*35. Faça um algoritmo que calcule e mostre a área de um losango. Sabe-se que: A =
(diagonal_maior * diagonal_menor)/2*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float diagonal_maior,diagonal_menor,a;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Area do losango\n\n");
	printf("Insira aqui o valor da diagonal menor: ");
	scanf("%f",&diagonal_menor);
		printf("Insira aqui o valor da diagonal maior: ");
	scanf("%f",&diagonal_maior);
	
	a=(diagonal_maior * diagonal_menor)/2;
	
	system("cls");
	
	printf("Area do losango\n\n");
	printf("A area do losango é igual à %.2f",a);
		
		printf("\n\n");
		system("pause");
}
