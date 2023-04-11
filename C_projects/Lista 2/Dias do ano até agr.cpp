/*7. Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do
ano. Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.*/

#include<conio.h>  
#include<stdio.h>  
#include<iostream> 
#include<locale.h>
#include <stdlib.h>

int dia,mes,diastotais;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Dias do ano(totais)\n\n");
	printf("Insira o total de dias até o momento: ");
	scanf("%i",&dia);
	
	printf("\nInsira o total de meses até o momento: ");
	scanf("%i",&mes);
	
	/*if(mes > 0){
		mes*30;
	}
	*/
	if(mes>12){
		printf("O numero de meses é maior q 12, inexistente\n");
		printf("\n\n");
		system("pause");
		exit(1);
	}
	
	diastotais = ((mes*30) + dia);
	printf("\n\nO numero total de dias do ano até agora é: %i",diastotais);
	
	printf("\n\n");
	system("pause");
	
}

