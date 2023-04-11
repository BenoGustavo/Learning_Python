/*Questão 1 - 01 – Ana e Maria, cada uma delas tem um cofrinho com muitas moedas, e elas
querem saber quantos reais conseguiram poupar individualmente e juntas. Faça
um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor
total economizado por Ana, por Maria e por ambas, em reais. Considere que elas
somente guardaram moedas de 50 centavos e 1 real. Construa um algoritmo
codificado na linguagem C que leia para Ana as respectivas quantidades de
moedas de cada valor, assim como para a Maria e por fim calcule o valor em
reais e centavos economizado por Ana, e por Maria e por ambas, mostrando nas
telas tais informações. (5,0 pontos) */


#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

float Rmaria,Rana,RT;
int c50,c100,c502,c102;
char sl;

main(){
	setlocale(LC_ALL,"portuguese");
	
	do{
		do{
			system("cls");
			printf("Conte as moedas de maria e ana\n\n");
			printf("Insira a quantidade de moedas de 50c e 1R$ de Maria, respectivamente: ");
			scanf("%i %i",&c50,&c100);
			printf("\nInsira a quantidade de moedas de 50c e 1R$ de Ana, respectivamente: ");
			scanf("%i %i",&c502,&c102);
			
			if(c50<0 || c100<0 || c502<0 || c102<0){
				system("cls");
				printf("Conte as moedas de maria e ana\n\n");
				printf("Apenas valores positivos são aceitos...\n");
				printf("Retornando...\n");
				system("pause");
			}
		}while(c50<0 || c100<0 || c502<0 || c102<0);
			
			Rmaria=c50*50+c100*100 ;Rana=c502*50+c102*100 ;Rmaria=Rmaria/100; Rana=Rana/100; RT=Rmaria+Rana;
			
			system("cls");
			printf("Conte as moedas de maria e ana\n\n");
			
			printf("Maria tem tinha [%i] 50c e [%i] 1R$ ou seja %.2fR$\n\n",c50,c100,Rmaria);
			printf("Ana tem tinha [%i] 50c e [%i] 1R$ ou seja %.2fR$\n\n",c502,c102,Rana);
			printf("O total de dinheiro acumulado é %.2fR$\n",RT);
	
			 printf("\n\nAperte qualquer tecla para retornar ou [N] para sair");
			 sl=getche();
			 sl=toupper(sl);
		}while(sl!='N');
		
		printf("\nsaindo...");
	
	printf("\n\n");
}
