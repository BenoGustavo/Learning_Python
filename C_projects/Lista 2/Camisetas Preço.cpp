/*Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo
vendida respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário
forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a
máquina informe quanto será o valor arrecadado.*/

#include<conio.h> 
#include<stdio.h>  
#include<iostream> 
#include<locale.h>

int pequeno,medio,grande,valortotal,valorp,valorm,valorg;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Exercicio camisetas, preço \n\n");
	
	printf("Digite aqui quantas camisetas de tamanho P foram compradas: ");
	scanf("%i",&pequeno);
	
	printf("\nDigite aqui quantas camisetas de tamanho M foram compradas: ");
	scanf("%i",&medio);
	
	printf("\nDigite aqui quantas camisetas de tamanho G foram compradas: ");
	scanf("%i",&grande);
	
	valorp = pequeno * 10; valorm = medio * 12; valorg = grande * 15;
	
	valortotal = valorp + valorm + valorg;
	
	system("cls");
	
	printf("A quantidade de camisas P compradas de %i\n",pequeno);
	printf("A quantidade de camisas M compradas de %i\n",medio);
	printf("A quantidade de camisas G compradas de %i\n",grande);
	printf("\nO valor total da sua compra foi %iR$\n\n",valortotal);
	
	printf("\n\n");
	system("pause");
}
