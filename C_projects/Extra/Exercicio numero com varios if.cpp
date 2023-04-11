//1. Faça um programa em "C" que lê dois valores e imprime:
/*- se o primeiro valor for menor que o segundo, a lista de valores do primeiro até
o segundo;
 - se o primeiro valor for menor que o segundo a lista de valores do segundo até
o primeiro em ordem decrescente;
 - se ambos forem iguais a mensagem "valores iguais".*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

int n1,n2,numenor;
char op;

main(){
	setlocale(LC_ALL,"portuguese");
	
	do{
		
		system("cls");
	
	printf("Exercicio brabo\n\n");
	printf("Insira dois valores: ",n1,n2);
	scanf("%i %i",&n1,&n2);
	
	if(n1<n2){
		numenor=n1;
	}
	
	if(n2<n1){
		numenor=n2;
	}
	
	if(n1==n2){
		printf("Os valores são iguais...\n");
		printf("\nDeseja voltar? [S] OR [N]");
	break;
	}
	
	
	while(numenor>0){
		printf("\nO menor número é: %i",numenor);
		numenor=numenor-1;
	}
	
		printf("\n\nDeseja voltar? [S] OR [N]");
		op=getche();
		op=toupper(op);
}while(op != 'N');

printf("Saindo...");
	
	printf("\n\n");
	system("pause");
}
