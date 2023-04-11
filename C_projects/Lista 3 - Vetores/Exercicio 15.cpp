/*15. Leia um vetor de 10 posições e verifique se existem valores iguais e os
escreva.*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

int q,igual;
char inicio,op;

main(){
	setlocale(LC_ALL,"portuguese");
	
	inicio:
		system("cls");
	
	printf("Vetores - Exercicio 15\n\n");
	printf("Insira quantos vetores você deseja: ");
	scanf("%i",&q);
	
	int vet[q];
	
	for(int i=0;i<q;i++){
		vet[i]=rand() % q+q;
	}
	
	system("cls");
	printf("Vetores - Exercicio 15\n\n");
	
	for(int i=0;i<q;i++){
		printf("Vetor[%i] = %i\n",i,vet[i]);
	}
	
	printf("\nVetores iguais: ");
	
	for(int i=0;i<q;i++){
		for(int j=0;j<q;j++){
			if(vet[i]==vet[j] && j != i && vet[j] != igual){
				printf("%i,",vet[j]);
				igual = vet[j];
			}
		}
	}
	
	printf("\n\nNos indices: ");
	
	for(int i=0;i<q;i++){
		for(int j=0;j<q;j++){
			if(vet[i]==vet[j] && j != i && i != igual){
				printf("%i,",i);
				igual = i;
			}
		}
	}
	
	printf("\n\nPressione qualquer tecla para retornar ou 'N' para sair.\n");
	op=getche();
	op=toupper(op);
	
	if(op=='N'){
		exit(0);
	}else{
		goto inicio;
	}
	
}
