/*16. A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias
de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de
queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um
algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as
quantidades (em quilos) de queijo, presunto e carne necessários para compra.*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

int quantsand,queijo,presunto,hamburguer,peso,sandwitch,adicionalcarne,adicionalqueijo,adicionalpresunto,adicionalcarne2,adicionalqueijo2,adicionalpresunto2,queijokg,presuntokg,hamburguerkg;
float quantqueijo,quantpresunto,quanthamburguer;

main(){
	setlocale(LC_ALL,"portuguese");
	
	queijo=50; presunto=50; hamburguer=100; sandwitch = ((queijo*2)+presunto+hamburguer);
	queijokg=0.005; presuntokg=0.005; hamburguerkg=0.01;
	
	printf("lanchonete Gostosura calculadora de alimentos (KG)\n\n");
	printf("Digite aqui a quantidade de sanduiches a serem feitos: ");
	scanf("%i",&quantsand);
	system("cls");
//	printf("lanchonete Gostosura calculadora de alimentos (KG)\n\n");
//	printf("Insira os adicionais:Carne, queijo, presunto respectivamente: ");
//	scanf("%i %i %i",&adicionalcarne,&adicionalqueijo,&adicionalpresunto);
	
	adicionalcarne2=adicionalcarne; adicionalqueijo2=adicionalqueijo; adicionalpresunto2=adicionalpresunto;
	
{
/*	while(adicionalcarne>0){
	if(adicionalcarne>0){
		hamburguer = hamburguer+hamburguer;
		adicionalcarne = adicionalcarne-1;
	}
//}
//while(adicionalqueijo>0){
	if(adicionalqueijo>0){
		queijo = (queijo+(queijo*2));
		adicionalqueijo=adicionalqueijo-1;
	}
//}
//while(adicionalpresunto>0){
	if(adicionalpresunto>0){
		presunto = presunto+presunto;
		adicionalpresunto=adicionalpresunto-1;
	}
//}
*/	
}
	quantqueijo = ((quantsand*(queijo*2))/1000);
	quantpresunto = ((quantsand*presunto)/1000);
	quanthamburguer = ((quantsand*hamburguer)/1000);
/*	
	//	while(adicionalcarne>0){
	if(adicionalcarne>0){
		quanthamburguer = quanthamburguer+hamburguerkg;
	}
//}
//while(adicionalqueijo>0){
	if(adicionalqueijo>0){
		quantqueijo = (quantqueijo+(queijokg*2));
	}
//}
//while(adicionalpresunto>0){
	if(adicionalpresunto>0){
		quantpresunto = quantpresunto+presuntokg;
	}
//}
*/	
	
	system("cls");
	
//	printf("lanchonete Gostosura calculadora de alimentos (KG)\n\n");
//	printf("Seus adicionais são:%i Carne, %i Queijo, %i Presunto\n",adicionalcarne2,adicionalqueijo2,adicionalpresunto2);
		
	
	printf("A quantidade necessaria de carne é: %.2fKG\nA quantidade necessaria de queijo é: %.2fKG\nA quantidade necessaria de presunto é: %.2fKG\n",quanthamburguer,quantqueijo,quantpresunto);
	
	
	printf("\n\n");
	system("pause");
}
