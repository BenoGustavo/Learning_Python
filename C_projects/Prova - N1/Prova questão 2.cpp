/*Questão 2 - 02 – Uma empresa de desenvolvimento de software está codificando um sistema
de geração de folhas de pagamento dos colaboradores de uma empresa de
Suprimentos de Informática, para isto pede alguns dados de entrada do setor de
gestão de pessoas e assim gera a folha do mês. Pede o Nome do Colaborador,
quantidade de horas trabalhadas no mês, valor da Hora/trabalho, qual o % de
INSS a descontar e qual o % do Imposto de renda a descontar. Com estas
informações inseridas no sistema, este gera e mostra na tela a folha do
colaborador com os seguintes dados: Nome, Horas/Trabalhas, Valor Hora,
salário bruto, % INSS, % IR, e salário líquido. (5,0 pontos) */

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

char sl,func[30];
float ht,h,inss,imprenda,sal,descinss,descimprenda,salb;

main(){
	setlocale(LC_ALL,"portuguese");
	
	do{
		do{
			system("cls");
			printf("Folhas de pagamento\n\n");
			printf("Insira o primeiro nome do funcionario: ");
			scanf("%s",&func);
			
			printf("\nInsira a quantidade de horas trabalhadas: ");
			scanf("%f",&ht);
			
			printf("\nInsira o valor da hora: ");
			scanf("%f",&h);
			
			printf("\nInsira o desconto do INSS (sem porcentagem %): ");
			scanf("%f",&inss);
			
			printf("\nInsira o desconto do imposto de renda (sem porcentagem %): ");
			scanf("%f",&imprenda);
			
			if(ht<0 || h<0 || inss<0 || imprenda<0){
				system("cls");
				printf("Folhas de pagamento\n\n");
				printf("Insira valores validos...\n");
				printf("Retornando...\n\n");
				system("pause");
			}
			}while(ht<0 || h<0 || inss<0 || imprenda<0);
			
			inss=inss/100; imprenda=imprenda/100; sal=ht*h; salb=sal ;descinss=sal*inss; descimprenda=sal*imprenda; sal=sal-descinss; sal=sal-descimprenda;
			
			system("cls");
			printf("Folhas de pagamento\n\n");
			
			printf("O colaborador %s \n\n",func);
			printf("Trabalhou por %.2f horas \n",ht);
			printf("Sua hora trabalhada vale %.2fR$ \n",h);
			printf("Tem o salário bruto de %.2fR$ \n",salb);
			printf("Recebe desconto de %.2f do INSS \n",descinss);
			printf("Recebe desconto de %.2f do IR [Imposto de renda] \n\n",descimprenda);
			printf("Portanto tem um salário líquido de: %.2f \n\n",sal);
			
	
			 printf("\n\nAperte qualquer tecla para retornar ou [N] para sair");
			 sl=getche();
			 sl=toupper(sl);
		}while(sl!='N');
		
		printf("\nsaindo...");
	
	printf("\n\n");
}
