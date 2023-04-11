//Algoritmo preço automóvel
//O preço de um automóvel é calculado pela soma do preço de fábrica com o preço dos
//impostos (45% do preço de fábrica) e a percentagem do revendedor (28% do preço de fábrica).
//Faça um algoritmo que leia o nome do automóvel e o preço de fábrica e imprima o nome do
//automóvel e o preço final.

//Bibliotecas
#include<conio.h>  //inclusão da biblioteca conio - comandos I/O - Input/Output - Entrada e saída
#include<stdio.h>  //inclusão da biblioteca stdio - comandos de tela I/O
#include<iostream> //inclusão da biblioteca mais completa
#include<locale.h>

//Declarar variaveis
float PrecoDeFabrica;
float Impostos;
float Revendedor;
float Precofinal;
float Veiculo;

//Principal
main(){
	
printf("Digite aqui a marca do veiculo (SEM ESPACOS).\n");
scanf("%s" ,&Veiculo);	

printf("Digite o preco do veiculo.(SEM PONTOS)\n");
scanf ("%f" ,&PrecoDeFabrica);

Impostos = PrecoDeFabrica * 0.45;

Revendedor = PrecoDeFabrica * 0.28;

Precofinal = PrecoDeFabrica + Impostos + Revendedor;

printf("\n Tem o valor de fabrica: %2.2f",PrecoDeFabrica);
printf("\n E recebe 45 porcento desse valor em impostos: %2.2f",Impostos);
printf("\n Tendo a taxa do Revendedor de 28 porcento com base no Preco De Fabrica: %2.2f",Revendedor);
printf("\n Tem o valor de final de %2.2f",Precofinal);
printf("\n A marca do seu veiculo eh %s",Veiculo);

printf("\n\n");
system("pause");
}
