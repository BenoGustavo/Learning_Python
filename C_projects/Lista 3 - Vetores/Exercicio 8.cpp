/* 8. Leia um vetor de 40 posições. Contar e escrever quantos valores pares ele
possui. */

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

char inicio,op;
int q,par;

main(){
	setlocale(LC_ALL,"portuguese");
	
	inicio:
	
	system("cls");
	printf("Vetores - Exercicio 8\n\n");
	printf("Quantos vetores você deseja?\n");
	scanf("%i",&q);
	
int vet[q]; //Criar o vetor depois, por conta que o mesmo so pode ser gerado depois de existir um valor dentro de q
	
	for(int i=0;i<q;i++){
		vet[i] = rand() % q+q;
	}
	
	for(int i=0; i<13; i++){
        for(int a=0; a<13; a++){
         if(i == a)
          continue;
          if(vet[i] == vet[i])
             vet[a] = rand()%1000;
       	}
   	}
	
	for(int i=0;i<q;i++){
	if(vet[i] % 2 == 0){
			par=par+1;
		}
	}
	
	system("cls");
	printf("Vetores - Exercicio 8\n\n");
	
	printf("O vetor:\n");
	for(int i=0;i<q;i++){
		printf("Vetor [%i] = %i\n",i,vet[i]);
	}
	printf("\nTem %i valores pares, estando eles nos indices:",par);
	for(int i=0;i<q;i++){
		if(vet[i] % 2 == 0){
			printf(" %i,",i);
		}
	}
	
	printf("\n\n\nPressione qualquer tecla para retornar ou 'N' para sair.\n");
	op=getche();
	op=toupper(op);
	
	if(op=='N'){
		exit(0);
	}else{
		goto inicio;
	}
}
