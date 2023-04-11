//Algorismo que calcula o IMC de um atleta

//Bibliotecas
#include<conio.h>  //inclusão da biblioteca conio - comandos I/O - Input/Output - Entrada e saída
#include<stdio.h>  //inclusão da biblioteca stdio - comandos de tela I/O
#include<iostream> //inclusão da biblioteca mais completa
#include<locale.h>

//declaração variáveis
char Nome [30];
float Peso,Altura,Imc;
int Idade;

//Inicio
main(){

	printf("Nome do atleta\n");
scanf ("%s" ,&Nome);

printf("Digite o peso do atleta em KG\n");
scanf ("%f" ,&Peso);

printf("Digite a altura do atleta em metros\n");
scanf ("%f" ,&Altura);

printf("Digite a idade do atleta\n");
scanf ("%i" ,&Idade);

fflush(stdin);// limpa buffer

Imc = (Peso/ (Altura*Altura));

printf("\n O Atleta: %s",Nome);
printf("\n Com a idade de %i anos",Idade);
printf("\n Com a altura de: %2.2f metros",Altura);
printf("\n Com o peso de : %2.2f kg",Peso);
printf("\n Apresentou IMC = %2.2f",Imc);

//Calculo IMC
if(Imc <= 17.00 ){
	printf("\n Muito abaixo do peso indicado - IMC: %2.2f",Imc);
}
if((Imc > 17.00 )&&(Imc <= 18.49 )){
	printf("\n Abaixo do peso indicado - IMC: %2.2f",Imc);
}
if((Imc > 18.49 )&&(Imc <= 25.00 )){
	printf("\n Peso Normal - IMC: %2.2f",Imc);
}
if((Imc > 25.00 )&&(Imc <= 30.00 )){
	printf("\n Acima do Peso - IMC: %2.2f",Imc);
}
if((Imc > 30.00 )&&(Imc <= 35.00 )){
	printf("\n Obsidade I - IMC: %2.2f",Imc);
}
if((Imc > 35.00 )&&(Imc <= 40.00 )){
	printf("\n Obsidade II- IMC: %2.2f",Imc);
}
if((Imc >= 40)){
	printf("\n Obesidade III - IMC: %2.2f",Imc);
}

printf("\n\n");
system("pause");
}
