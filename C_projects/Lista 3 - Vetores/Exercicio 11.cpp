/*11. Leia um vetor de 40 posições e acumule os valores do primeiro elemento
no segundo, deste no terceiro e assim por diante. Ao final, escreva o vetor
obtido.*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

char inicio,op;
int vet[39];

main(){
	setlocale(LC_ALL,"portuguese");
	
	inicio:
	
	system("cls");
	printf("Vetores - Exercicio 11\n\n");
	
	for(int i=0;i<40;i++){
		vet[i] = rand() % 101;
	}
	
	for(int i=0; i<40; i++){
        for(int a=0; a<40; a++){
         if(i == a)
          continue;
          if(vet[i] == vet[i])
             vet[a] = rand()%101;
       	}
   	}
   	
   	printf("Vetor original\n\n");
   	for(int i=0;i<40;i++){
   		printf("Vetor Original [%i] = %i\n",i,vet[i]);
	   }
	
	for(int i=0;i<40;i++){
		if(i>0){
			vet[i] = vet[i] + vet[i-1];
		}
	}
	
	printf("\nVetor Modificado\n\n");
   	for(int i=0;i<40;i++){
   		printf("Vetor MOD[%i] = %i\n",i,vet[i]);
	   }
	   
	   printf("\nPressione qualquer tecla para retornar ou 'N' para sair.\n");
	op=getche();
	op=toupper(op);
	
	if(op=='N'){
		exit(0);
	}else{
		goto inicio;
	}
}
