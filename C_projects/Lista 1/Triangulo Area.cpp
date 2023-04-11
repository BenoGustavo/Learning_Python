//Faça um algoritmo para ler a base e a altura de um triângulo. Em seguida, escreva a área do mesmo. Área = (Base * Altura) / 2

#include<conio.h> 
#include<stdio.h>  
#include<iostream>

//Declarar as variaveis
float Base,Altura,Area;

//Inicio
main(){
	
	printf("Coloque a BASE do triangulo em CM\n");
scanf ("%f",&Base);

printf("Coloque a Altura do triangulo em CM\n");
scanf ("%f",&Altura);

Area = ((Base * Altura)/2);

printf("\nA area do seu triangulo retangulo eh %2.2f cm ao quadrado",Area);

printf("\n\n");
system("pause");
}
