/*21. A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml,
garrafa de 600 ml e garrafa de 2 litros. Se um comerciante compra uma determinada
quantidade de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele
comprou.*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

int quant350,quant600,quant2L;
float Ltotal;

main(){
	printf("Calculadora de litros de refrigerante\n\n");
	printf("Digite aqui a quantidade de latas de 350 ml, garrafa de 600 ml, garrafa de 2 litros: ");
	scanf("%i %i %i",&quant350,&quant600,&quant2L);
	
while(quant350>0 && quant600>0 && quant2L>0 ){	
	if(quant350>0){
		Ltotal=Ltotal+350;
		quant350=quant350-1;
	}
	if(quant600>0){
		Ltotal=Ltotal+600;
		quant600=quant600-1;
	}
	if(quant2L>0){
		Ltotal=Ltotal+2000;
		quant2L=quant2L-1;
	}
}
system("cls");
printf("Calculadora de litros de refrigerante\n\n");

Ltotal = Ltotal/1000;

	printf("A quantidade de litros total é de: %.2f",Ltotal);
	
	printf("\n\n");
	system("pause");
}
