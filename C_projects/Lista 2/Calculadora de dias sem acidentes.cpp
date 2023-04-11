/*11. Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias. Faça um
algoritmo para converter este tempo em anos, meses e dias. Assume que cada mês possui
sempre 30 dias.*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

int DiasSemAcidentes,anos,meses,dias,dias2;

main(){
	setlocale(LC_ALL,"portuguese");//uso do protuguês nos textos
	printf("Calculadora de total de dias sem acidentes\n\n");
	printf("Insira aqui a quantidade de dias sem acidentes: ");
	scanf("%i",&DiasSemAcidentes);
	
	
	
	anos == 0;dias == 0;meses == 0;dias2=DiasSemAcidentes;
	
	while(DiasSemAcidentes>0){
		if(DiasSemAcidentes>=365){
			DiasSemAcidentes = DiasSemAcidentes - 365;
			anos = anos+1;
		}
		else if(DiasSemAcidentes<365 && DiasSemAcidentes>=30){
			DiasSemAcidentes = DiasSemAcidentes - 30;
			meses = meses+1;
		}
		else if(DiasSemAcidentes<30 && DiasSemAcidentes>0){
			DiasSemAcidentes = DiasSemAcidentes - 1;
			dias = dias+1;
		}
	}
	
	system("cls");
	printf("Calculadora de total de dias sem acidentes\n\n");
	
	printf("Acidentes não acontecem a mais de %i anos, %i meses, %i dias, totalizando %i dias",anos,meses,dias,dias2);
	printf("\n\n");
	system("pause");
}
