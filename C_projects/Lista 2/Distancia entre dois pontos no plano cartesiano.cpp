/*10. Construa um algoritmo para calcular a distância entre dois pontos do plano cartesiano.
Cada ponto é um par ordenado (x,y).*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

float X1,Y1,X2,Y2,distancia;

main(){
	setlocale(LC_ALL,"portuguese");//uso do protuguês nos textos
	printf("Distancia entre dois pontos no plano cartesiano\n\n");
	
	printf("Digite aqui os valores do ponto 1 (x,y): ");
	scanf("%f %f",&X1,&Y1);
	
	system("cls");
	
	printf("Distancia entre dois pontos no plano cartesiano\n\n");
	
	printf("Digite aqui o valor do ponto 2 (x,y): ");
	scanf("%f %f",&X2,&Y2);
	
	system("cls");
	
	distancia = sqrt(pow((X1-X2),2)+pow((Y1-Y2),2));
	
	printf("Distancia entre dois pontos no plano cartesiano\n\n");
	
	printf("A distancia entre o ponto 1 (%.2fx,%.2fy) e ponto 2 (%.2fx,%.2fy) é: %.2f",X1,Y1,X2,Y2,distancia);
	
	printf("\n\n");
	system("pause");
	
	//printf("%.2f X1 / %.2f Y1 / %.2f X2 / %.2f Y2",X1,Y1,X2,Y2);
	//printf("Distancia %.2f",distancia);
}
