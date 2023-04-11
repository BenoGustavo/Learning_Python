/*12. Faça um algoritmo para ler o salário de um funcionário e aumentá-lo em 15%. Após o
aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento e o
salário final.*/

#include<conio.h> 
#include<stdio.h>  
#include<iostream> 
#include<locale.h>
#include<math.h>

float salario,imposto,aumento,salariototal,salarioaumento;

main(){
	setlocale(LC_ALL,"portuguese"); //Mudar idioma para portugues
	printf("Calculadora de salario\n\n");
	printf("Insira aqui seu salario (com , apenas para centavos): ");
	scanf("%f",&salario);
	
	aumento = salario*0.15;
	
	salarioaumento = salario+aumento;
	
	imposto = salarioaumento*0.08;
	
	salariototal=((salario+aumento)-imposto);
	
	system("cls");
	
	printf("\nO seu salario é: %.2fR$, Voce paga: %.2fR$ de imposto, Seu salario final: %.2fR$",salario,imposto,salariototal);
	
	printf("\n\n");
	system("pause");
	
}
