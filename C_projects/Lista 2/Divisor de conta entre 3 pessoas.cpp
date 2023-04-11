/*15. Três amigos, Carlos, André e Felipe, decidiram rachar igualmente a conta de um bar. Faça
um algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça
com que Carlos e André não paguem centavos. Ex: uma conta de R$101,53 resulta em R$33,00
para Carlos, R$33,00 para André e R$35,53 para Felipe.*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

char nome1[30],nome2[30],nome3[30];
float R$total,centavos,conta,contacomc;
int totalsemc;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Distribuidor de preço entre 3 pessoas\n\n");
	
	printf("Digite o nome de 3 pessoas sendo o ultimo quem ira pagar os centavos: ");
	scanf("%s %s %s",&nome1,&nome2,&nome3);
	
	printf("\nDigite o valor total a pagar: ");
	scanf("%f",&R$total);
	
	
	conta = R$total/3; totalsemc = conta; centavos = conta-totalsemc;
	
	contacomc = conta+centavos+centavos;
	
	system("cls");
	
	printf("Distribuidor de preço entre 3 pessoas\n\n");
	printf("O valor total da compra é de: %.2f",R$total);
	printf("\n\n%s ira pagar o valor inteiro de: %i ",nome1,totalsemc);
	printf("\n%s ira pagar o valor inteiro de: %i ",nome2,totalsemc );
	printf("\n%s ira pagar o valor quebrado de: %.2f",nome3,contacomc );
	
	//printf("\n\n\n%s , %s , %s , %.2f , %.2f , %i, %.2f",nome1, nome2 , nome3 , R$total, centavos, totalsemc, contacomc );// - teste de variaveis
	
	printf("\n\n");
	system("pause");
}
