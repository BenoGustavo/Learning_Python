/*39. João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e
C2=R$120,00) que estão atrasadas. Como as contas estão atrasadas, João terá de pagar multa
de 2% sobre cada conta. Faça um algoritmo que calcule e mostre quanto restará do salário do
João;*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float sal,c1,c2,atrasoc1,atrasoc2,ressal;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Calculadora de contas atrasadas\n\n");
	printf("Insira aqui seu salário: ");
	scanf("%f",&sal);
	printf("Insira o valor de duas contas: ");
	scanf("%f %f",&c1,&c2);
	
	atrasoc1=c1*0.02; atrasoc2=c2*0.02; c1=c1+atrasoc1; c2=c2+atrasoc2; ressal=sal-c1-c2;
	
	system("cls");
	printf("Calculadora de contas atrasadas\n\n");
	printf("Seu salário é de %.2fR$, após pagar a multa de %.2fR$ da conta1 [%.2f] e %.2fR$ da conta2 [%.2f] seu salário será de %.2f",sal,atrasoc1,c1,atrasoc2,c2,ressal);
	
	printf("\n\n");
	system("pause");
}
