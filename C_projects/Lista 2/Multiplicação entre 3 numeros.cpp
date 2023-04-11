/*26. Faça um algoritmo que receba três números, calcule e mostre a multiplicação desses
números.*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float v1,v2,v3,r,multipl,multipl2;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Multiplicação entre 3 números\n\n");
	printf("Insira aqui os 3 valores a serem multiplicados: ");
	scanf("%f %f %f",&v1,&v2,&v3);
	
	r=v1*v2;
	multipl=v1*v2*v3;
	
	system("cls");
	printf("Multiplicação entre 3 números\n\n");
	printf("A sua multiplicação de %.2f e %.2f, tem como resultado %.2f, que multiplicado por %.2f, tem o resultado de: %.2f",v1,v2,r,v3,multipl);
	
	printf("\n\n");
	system("pause");
	
}
