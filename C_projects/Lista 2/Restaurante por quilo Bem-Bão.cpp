/*6. O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um
algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.
Assume que a balança já desconte o peso do prato.*/

#include<conio.h>
#include<stdio.h> 
#include<iostream>
#include<locale.h>

float  ValorDoPrato, Quilo;

main(){
setlocale(LC_ALL,"portuguese");
printf("Bem Vindo ao restaurante a quilo Bem-Bom\n\n");

printf("Insira aqui o peso da sua comida em quilos\n:");
scanf("%f",&Quilo);

ValorDoPrato = 12*Quilo;

system("cls");

printf("O peso do seu prato é igual a %.1f, portanto o valor do mesmo é igual a %.2fR$",Quilo,ValorDoPrato);

printf("\n\n");
system("pause");

}
