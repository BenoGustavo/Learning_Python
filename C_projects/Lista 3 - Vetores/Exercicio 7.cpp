/*7. Leia um vetor de 20 posições e em seguida um valor X qualquer. Seu
programa deverá fazer uma busca do valor de X no vetor lido e informar a
posição em que foi encontrado ou se não foi encontrado.*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

int vet[19],x,acerto;
char aaa,inicio;
int y;

main(){
	setlocale(LC_ALL,"portuguese");
	
	inicio:
		system("cls");
	
	printf("Vetores - Exercicio 7\n\n");
	
	acerto=0;
	
	printf("Insira seu chute. [0-200]\n");
	scanf("%i",&y);
	
	system("cls");
	
	
	for(int i=0;i<20;i++){
		
		vet[i] = rand() % 201;
	}
	
	//verificar repetição
	
	for(int i=0; i<16; i++){
        for(int a=0; a<16; a++){
    	if(i == a)
        continue;
        if(vet[i] == vet[i])
        vet[a] = rand()%201;
        }
    }
    
    for(int i=0;i<20;i++){
    	if(y == vet[i]){
    		acerto=1;
		}
	}
	
	printf("Vetores - Exercicio 7\n\n");
	
	for(int i=0;i<20;i++){
		printf("Vetor[%i] = %i\n",i,vet[i]);
	}
	
	switch(acerto){
		case 1:{
			printf("\nParabens, valor acertado\n");
			printf("O valor %i foi visto nos indices: ",y);
		
			for(int i=0;i<20;i++){
			if(vet[i] == x){
			printf("%i",i);
			}
		}
			break;
		}
		case 0:{
			if(acerto==0){
			printf("Você ERROU, o valor [%i] não existe dentro do vetor",y);
			}
			
			break;
		}
	}
	
	printf("\n\nAperte qualquer botão para retornar ou 'N' para sair.\n");
	aaa=getche();
	aaa=toupper(aaa);
	
	switch(aaa){
		case 'N':{
			system("cls");
			printf("Saindo...\n");
			system("cls");
			exit(0);
		break;
		}
		default:{
			goto inicio;
			break;
		}
	}
}
