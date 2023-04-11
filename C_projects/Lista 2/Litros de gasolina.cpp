/*5. Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para
ler o preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu
colocar no tanque.*/

//Preço L da gasolina = 5.4 R$

#include<conio.h>
#include<stdio.h> 
#include<iostream>
#include<locale.h>

float Dinheiro,Ldegasolina,valorfinal;

main(){
	setlocale(LC_ALL,"portuguese");
	
	printf("Gasolina\n\n");
	printf("Coloque aqui o valor em reais desejado de gasolina - Valor da gasolina: 5,4R$\n");
	scanf("%f",&Dinheiro);
	
	Ldegasolina = Dinheiro/5,40;
	
	printf("Você colocou %.2fR$ em gasolina, isso deu %.2f Litros",Dinheiro,Ldegasolina);
	
	printf("\n\n");
	system("pause");
}


