/*5 – Algoritmo PA – Progressão Aritmética
Faça um programa que imprima os elementos de uma PA e o somatório da mesma dados :
primeiro termo , numero de termos e razão.*/

#include<conio.h> 
#include<stdio.h>  
#include<iostream> 
#include<locale.h>

int PrimeiroTermo,NdeTermos,razao,somatorio,PA;

main(){
	setlocale(LC_ALL,"portuguese"); //Mudar idioma para portugues
	
	printf("Progressão aritmetica\n\n");
	printf("Digite o valor do primeiro termo: ");
	scanf("%i",&PrimeiroTermo);
	
	printf("\nDigite o número de termos: ");
	scanf("%i",&NdeTermos);
	
	printf("\nDigite a razâo: ");
	scanf("%i",&razao);
	
	system("cls");
	
	printf("A SUA PA É\n");
	
	printf("\nO 1° termo da PA é: %i",PrimeiroTermo);
	
	for(int i=2; i<=razao; i++){
		PA=PrimeiroTermo+razao;
		PrimeiroTermo=PA;
		printf("\nO %i° termo da PA é: %i",i,PA);
		
	}
	
	printf("\n\n");
	system("pause");
}
