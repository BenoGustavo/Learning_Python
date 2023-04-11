/*38. Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e
mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias;
d) a idade dessa pessoa em semanas.*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

int anos,meses,dias,semanas,select,total;

main(){
	setlocale(LC_ALL,"portuguese");
	select=0;
	printf("Conversor de idade em anos para meses,semanas,dias\n\n");
	printf("Selecione o que deseja (1)meses (2)semanas (3)dias: ");
	scanf("%i",&select);
			
			if(select>3){
		printf("\nComando invalido FECHANDO");
		printf("\n\n");
		system("pause");
		exit(1);
	}
	system("cls");
	printf("Conversor de idade em anos para meses,semanas,dias\n\n");
	printf("Insira aqui sua idade em anos: ");
	scanf("%i",&anos);
	
	//while(select>0 && select<4){
	if(select>0 && select<2){
		total=((anos*365)/30);
		printf("Sua idade(%i) em meses é %i",anos,total);
		select=select-1;
		printf("\n\n");
		system("pause");
		exit(1);
	}

		if(select>1 && select<3){
		total=((anos*365)/7);
		printf("Sua idade(%i) em semanas é %i",anos,total);
		select=select-2;
		printf("\n\n");
		system("pause");
		exit(1);
	}

		if(select>2 && select<4){
		total=anos*365;
		printf("Sua idade(%i) em dias é %i",anos,total);
		select=select-3;
		printf("\n\n");
		system("pause");
		exit(1);
	}
	
	printf("\n\n");
	system("pause");
}
