/*Construa um algoritmo em C que leia 10 numeros inteiros e localize 
o maior e o menor*/

#include<conio.h> 
#include<stdio.h>  
#include<iostream> 
#include<locale.h>

int numero,MaiorNum,MenorNum;

main(){
	setlocale(LC_ALL,"portugues"); //Mudar idioma para portugues
	system("cls");
	
	MenorNum=99999;
	MaiorNum=0;
	
	//Comandos novos
	
	for(int i=1; i<=10 ; i++){
		printf("\n numero[%i]: ",i);
		scanf("%i",&numero);
		if(numero < MenorNum){
			MenorNum=numero;
		}
		if(numero > MaiorNum){
			MaiorNum=numero;
	}
	
	} //final do for
	printf("\n NumMenor[%i]",MenorNum);
	printf("\n NumMaior[%i]",MaiorNum);
	
	printf("\n\n");
	system("pause");
}
