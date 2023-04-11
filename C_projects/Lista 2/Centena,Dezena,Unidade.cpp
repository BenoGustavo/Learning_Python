/*13. Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma:
CENTENA = x DEZENA = x UNIDADE = x*/

#include<conio.h> 
#include<stdio.h>  
#include<iostream> 
#include<locale.h>

int total,centena,dezena,unidade;

main(){
	setlocale(LC_ALL,"portuguese"); //Mudar idioma para portugues
	printf("Algoritmo que lê número interos e CENTENA = x DEZENA = x UNIDADE = x\n\n");
	printf("Insira aqui um número de até 3 digitos: ");
	scanf("%i",&total);
	
while(total > 0){
	
	if(total>=1000){
		printf("O número inserido é maior que 999 (mais que 3 digitos)\n\n");
		exit(1);
	}

else if(total>=100 && total <1000){
	total=total-100;
	centena=centena+1;
}
else if(total>=10&&total<=99){
	total=total-10;
	dezena=dezena+1;
}
else if(total>0&&total<=9){
	total=total-1;
	unidade=unidade+1;
}
}

	printf("Unidade:%i , Dezenas:%i , Centena:%i",unidade,dezena,centena);
	
	printf("\n\n");
	system("pause");
}
