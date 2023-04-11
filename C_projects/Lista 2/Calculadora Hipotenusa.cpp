/*40. Faça um algoritmo que receba o valor dos catetos de um triângulo, calcule e mostre o valor
da hipotenusa.formula a2 + b2 = c2 */

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float catMaior,catMenor,hip;

main(){
setlocale(LC_ALL,"portuguese");
printf("Calculadora de hipotenusa\n\n");
printf("Insira aqui o valor dos catetos menor e cateto maior: ");
scanf("%f %f",&catMaior,&catMenor);

hip = pow(catMaior,2)+pow(catMenor,2);

hip = sqrt(hip);

system("cls");

printf("Calculadora de hipotenusa\n\n");
printf("O valor da sua hipotenusa é %.2f",hip);

printf("\n\n");
system("pause");
}
