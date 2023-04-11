/*22. Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais conseguiu
poupar. Faça um algoritmo para ler a quantidade de cada tipo de moeda, e imprimir o valor
total economizado, em reais. Considere que existam moedas de 1, 5, 10, 25 e 50 centavos, e
ainda moedas de 1 real. Não havendo moeda de um tipo, a quantidade respectiva é zero.*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

int c1,c5,c10,c25,c50,c100,simenao,s,n;
float R$total;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Contador de moedas automatico\n\n");
	printf("Insira aqui a quantidade de moedas de 1¢, 5¢, 10¢, 25¢, 50¢, 1R$ (respectivamente): ");
	scanf("%i %i %i %i %i %i",&c1,&c5,&c10,&c25,&c50,&c100);
	
	R$total=0;
	
	s=1;
	n=2;
	
	while(c1>0 && c5>0 && c10>0 && c25>0 && c50>0 && c100>0){
		if(c1>0){
			c1=c1-1;
			R$total=R$total+1;
		}
		if(c5>0){
			c5=c5-1;
			R$total=R$total+5;
		}
		if(c10>0){
			c10=c10-1;
			R$total=R$total+10;
		}
		if(c25>0){
			c25=c25-1;
			R$total=R$total+25;
		}
		if(c50>0){
			c50=c50-1;
			R$total=R$total+50;
		}
		if(c100>0){
			c100=c100-1;
			R$total=R$total+100;
		}
	}
	
	R$total=R$total/100;
	
	system("cls");
	printf("Contador de moedas automatico\n\n");
	
	printf("Suas moedas resultam em um total de %.2fR$",R$total);
	
	printf("\n\nDeseja calcular novamente?(1)para sim ou (2)para não \n: ");
	scanf("%i",&simenao);
	
	switch (simenao){
		case 1:
			system("cls");
				printf("Contador de moedas automatico\n\n");
	printf("Insira aqui a quantidade de moedas de 1¢, 5¢, 10¢, 25¢, 50¢, 1R$ (respectivamente): ");
	scanf("%i %i %i %i %i %i",&c1,&c5,&c10,&c25,&c50,&c100);
	
	R$total=0;
	
	while(c1>0 && c5>0 && c10>0 && c25>0 && c50>0 && c100>0){
		if(c1>0){
			c1=c1-1;
			R$total=R$total+1;
		}
		if(c5>0){
			c5=c5-1;
			R$total=R$total+5;
		}
		if(c10>0){
			c10=c10-1;
			R$total=R$total+10;
		}
		if(c25>0){
			c25=c25-1;
			R$total=R$total+25;
		}
		if(c50>0){
			c50=c50-1;
			R$total=R$total+50;
		}
		if(c100>0){
			c100=c100-1;
			R$total=R$total+100;
		}
	}
	
	system("cls");
	printf("Contador de moedas automatico\n\n");
	
	R$total=R$total/100;
	
	printf("Suas moedas resultam em um total de %.2fR$",R$total);
	
	printf("\n\n");
	system("pause");
	
	exit;		
	
	case 2:
		system("cls");
		printf("Saindo...");
		exit;
	}
	
	printf("\n\n");
	system("pause");
	
	/*switch (expression)  {
    case constant1:
        // code to be executed if 
        // expression is equal to constant1;
        break;

    case constant2:
        // code to be executed if
        // expression is equal to constant2;
        break;
        .
        .
        .
        */
}
