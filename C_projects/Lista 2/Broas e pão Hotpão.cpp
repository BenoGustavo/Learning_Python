/*3. A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de
broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono
quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve guardar
numa conta de poupança (10% do total arrecadado). Você foi contratado para fazer os cálculos
para o dono. Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de
broas, e depois calcular os dados solicitados.*/

#include<conio.h>
#include<stdio.h> 
#include<iostream>
#include<locale.h>

float Valorbruto,Poupanca,VBMP,Pao,Broa;

main(){
	setlocale(LC_ALL,"portuguese");
	
	printf("Calculadora ultrasonica da padaria Hotpão.\r");
	
	printf("Coloque aqui a quantidade de pães vendidas no dia: ");
	scanf("%f",&Pao);
	
	printf("Coloque aqui a quantidade de broas vendidas no dia: ");
	scanf("%f",&Broa);
	
	Valorbruto = ((Pao * 0.12)+(Broa * 1.50));
	Poupanca = Valorbruto * 0.1;
	VBMP = Valorbruto - Poupanca;
	
	system("cls");
	
	printf("A quantidade de pães vendidas no dia é de %.0f",Pao);
	printf("\nA quantidade de broas vendidas no dia é de %.0f\n\n",Broa);
	printf("O valor bruto arrecadado em venda é %.2f\n",Valorbruto);
	printf("A quantidade a ser guardada na poupança é de %.2f\n",Poupanca);
	printf("A quantidade total arrecadada descontando a poupança é %.2f\n",VBMP);
	
	printf("\n\n");
	system("pause");
}


