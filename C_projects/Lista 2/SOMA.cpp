#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

int quantnum,select2,select3;
float num,somanum;
char select;

main(){
    setlocale(LC_ALL,"portuguese");

do{

    system("cls");

printf("Calculadora quatro operações basicas\n\n");
printf("Selecione a operação: [1] soma [2] subtração [3] taboada [4] divisão ");
scanf("%i",&select2);

    switch (select2){
    case 1:
do{
    quantnum = 0; num = 0; somanum = 0;

do{
    system("cls");
    printf("Calculadora de soma irrestrita\n\n");
    printf("Quantos números você deseja somar?: ");
    scanf("%i",&quantnum);

} while (quantnum <= 0);

for (int i = 1; i < quantnum + 1; i++)
{
    system("cls");
    printf("Calculadora de soma irrestrita\n\n");
    printf("Insira o [%i] número: ",i);
    scanf("%f",&num);

        somanum = somanum + num;
}

system("cls");

 printf("Calculadora de soma irrestrita\n\n");
 printf("A soma obtida dos algarismo inseridos eh: %.2f ",somanum);

    printf("\n\nDeseja calcular novamente? [S] ou [N]");
    select=getche();
    select=toupper(select);} while(select != 'N');

 printf("\n\nAperte qualquer botão para sair...");

 break;

 case 2: 
 do{
    quantnum = 0; num = 0; somanum = 0;

do{
    system("cls");
    printf("Calculadora de subtração irrestrita\n\n");
    printf("Quantos números você deseja subtrair?: ");
    scanf("%i",&quantnum);

} while (quantnum <= 0);

for (int i = 1; i < quantnum + 1; i++)
{
    system("cls");
    printf("Calculadora de subtração irrestrita\n\n");
    printf("Insira o [%i] número: ",i);
    scanf("%f",&num);

        somanum = somanum - num;
}

system("cls");

 printf("Calculadora de soma irrestrita\n\n");
 printf("A soma obtida dos algarismo inseridos eh: %.2f ",somanum);


    printf("\n\nDeseja calcular novamente? [S] ou [N]");
    select=getche();
    select=toupper(select);
 } while(select != 'N');
 

 printf("\n\nAperte qualquer botão para sair...");

 break;

case 3:
float num,numtotal,div;
int TDN;

do{

    num=0;numtotal=0;div=0;
    TDN=0;

system("cls");
printf("Tabuada automatica\n\n");
	printf("Insira aqui o número da tabuada desejada: ");
	scanf("%f",&num);
	printf("Insira aqui até que número você deseja sua tabuada: ");
	scanf("%f",&numtotal);
	
	TDN=numtotal;
	
	system("cls");
	
	printf("Tabuada automatica\n\n");
	while(numtotal>0){
		if(numtotal>0){
		div=num*numtotal;
		printf("\n%.2f*%.2f - RESULTADO: %.2f N(%i)",num,numtotal,div,TDN);
		TDN=TDN-1;
		numtotal=numtotal-1;
	}
	}
	printf("\nSua tabuada do %.2f foi finalizada",num);

    printf("\n\nDeseja calcular novamente? [S] ou [N]");
    select=getche();
    select=toupper(select);
 }while(select != 'N');
	
    printf("\n\nAperte qualquer botão para sair...");

    break;

    case 4: 
    float numad,divisor,res;
do{
    numad=0;divisor=0;res=0;

system("cls");

    printf("Calculadora de divisão automatica\n\n");
    printf("Ïnsira o número que você deseja divir: ");
    scanf("%f",&numad);

system("cls");

    printf("Calculadora de divisão automatica\n\n");
    printf("Ïnsira o divisor: ");
    scanf("%f",&divisor);

res =  numad/divisor;

system("cls");
printf("Calculadora de divisão automatica\n\n");
printf("O resultado da divisão entre %.2f e %.2f é %.2f",numad,divisor,res);

printf("\n\nDeseja calcular novamente? [S] ou [N]");
    select=getche();
    select=toupper(select);
 }while(select != 'N');
	
    printf("\n\nAperte qualquer botão para sair...");

default: 

system("cls");

printf("insira uma opção valida, retornando...\n\n");

system("pause");

}

}while (select2 > 4);

}