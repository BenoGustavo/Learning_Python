//Exercicio construir um algoritmo para ler o nome do aluno, 3Notas, e calcular a media.
//Se a média >=7.0 - apresentar uma mensagem dizendo "aprovado"
//se a média <4,0 - apresentar uma mensagem dizendo "Reprovado"
//se a média >=4.0 e média <7.0 apresentar uma mensagem que o aluno está "Em Exame"

#include<conio.h>
#include<stdio.h>
#include<iostream>

//Variaveis
char Aluno[30];
float Nota1;
float Nota2;
float Nota3;
float Media;

//Inicio
main(){ //comando da estrutura - Escopo - principal do programa
printf("\n Digite o nome do Aluno:");//escreva na tela("Digite o nome do Aluno:")
scanf("%s",&Aluno);//leia do teclado("operador %s tipo string-conjunto
// de char",& - ponteiro que localiza a posição na memória RAM da 
//variável Aluno
printf("\n Digite a Nota1:");
scanf("%f",&Nota1);//%f - tipo float
printf("\n Digite a Nota2:");
scanf("%f",&Nota2);//%f - tipo float
printf("\n Digite a Nota3:");
scanf("%f",&Nota3);//%f - tipo float
Media = (Nota1 + Nota2 + Nota3)/3;//cálculo da Média

if (( Media <= 7)&&( Media >= 4)){
	printf("\n Aluno em exame");
}
if ( Media >= 7){
	printf("\n Aluno aprovado");
}
if ( Media < 4){
	printf("\n Aluno reprovado");
}

printf("\n Nome do Aluno: %s",Aluno);//mostra na tela o valor da variável Aluno
printf("\n Nota1: %.2f",Nota1);//mostra na tela o valor da varíavel Nota1
printf("\n Nota2: %.2f",Nota2);//mostra na tela o valor da varíavel Nota2
printf("\n Nota2: %.2f",Nota3);//mostra na tela o valor da varíavel Nota3
printf("\n Media: %.2f",Media);//mostra na tela o valor da variável Media
printf("\n Nome do Aluno: %s tem a Média: %.2f",Aluno,Media);
printf("\n\n");//\n - new line  - nova linha
system("pause");//espera tecla enter para continuar
}
