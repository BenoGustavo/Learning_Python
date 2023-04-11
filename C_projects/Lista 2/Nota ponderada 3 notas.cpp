/*8. Faça um algoritmo para ler três notas de um aluno em uma disciplina e imprimir a sua média
ponderada (as notas tem pesos respectivos de 1, 2 e 3).*/

#include<conio.h>  
#include<stdio.h>  
#include<iostream> 
#include<locale.h>

char Nome[30];
float nota1,nota2,nota3,media;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Exercicio média ponderada.\n\n");
	printf("Coloque aqui o nome do aluno: ");
	scanf("%s",&Nome);
	
	fflush(stdin);
	
	printf("\nColoque aqui o primeira nota: ");
	scanf("%f",&nota1);
	
	printf("\nColoque aqui o segunda nota: ");
	scanf("%f",&nota2);
	
	printf("\nColoque aqui o terceira nota: ");
	scanf("%f",&nota3);
	
	nota1 = nota1*1; nota2 = nota2*2; nota3 = nota3*3;
	
	media = ((nota1 + nota2 + nota3)/3);
	system("cls");
	
	printf("O aluno %s",Nome);
	printf("\n\nTeve como media %.2f",media);
	
	printf("\n\n");
	system("pause");
}
