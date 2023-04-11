/*13. Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma:
CENTENA = x DEZENA = x UNIDADE = x*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

int centena,dezena,unidade,vtotal,vtotal2;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Distribuidora de unidades\n\n");
	printf("Digite aqui um valor de 0 à 999: ");
	scanf("%i",&vtotal);

centena == 0; dezena ==0; unidade ==0;vtotal2 = vtotal;

	if(vtotal>999){
	printf("Seu valor é maior que 3 digitos (999), favor colocar um valor valido");
	exit(1);
	}
	
	while(vtotal>0){
		 if(vtotal>99){
			vtotal = vtotal - 100;
			centena = centena + 1;
		}
		else if(vtotal>9&&vtotal<100){
			vtotal = vtotal - 10;
			dezena = dezena + 1;
		}
		else if(vtotal>0&&vtotal<10){
			vtotal = vtotal -1;
			unidade = unidade + 1;
		}
	}

	printf("O seu número (%i) tem %i unidades, %i dezenas, %i centenas",vtotal2,unidade,dezena,centena);
	printf("\n\n");
	system("pause");
}
