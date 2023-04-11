/*19. A granja Frangotech possui um controle automatizado de cada frango da sua produção. No
pé direito do frango há um anel com um chip de identificação; no pé esquerdo são dois anéis
para indicar o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa
R$4,00 e o anel de alimento custa R$3,50, faça um algoritmo para calcular o gasto total da
granja para marcar todos os seus frangos.*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float chipID,chipAlimento,chiptotal,quantchipalimento;
int frangos;

main(){
	printf("Frangotech identificador de quantidade de chips\n\n");
	printf("Digite aqui a quantidade de frangos que vão receber um chip: ");
	scanf("%i",&frangos);
	
	chipID = frangos * 4;
	
	chipAlimento = ((frangos*2)*3.50);

	chiptotal = chipID+chipAlimento;
	
	quantchipalimento = frangos*2;
	
	
	
	printf("\n\n");
	system("pause");
}
