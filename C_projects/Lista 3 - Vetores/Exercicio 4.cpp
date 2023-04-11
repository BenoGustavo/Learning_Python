/*
4 - Leia um vetor de 12 posições e em seguida ler também dois valores X e Y
quaisquer correspondentes a duas posições no vetor. Ao final seu programa
deverá escrever a soma dos valores encontrados nas respectivas posições X e
Y.
*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

char inicio,iniciop;
int op,vet[12],x,y,op2;

main(){
	setlocale(LC_ALL,"portuguese");
	inicio:
		system("cls");
	
	printf("Vetores, Exercicio 4\n\n");
	printf("Menu:\n");
	printf("1 - Inserir os valores manualmente\n");
	printf("2 - Aleatorizar os valores");
	op=getche();
	
	if(op>'2'){
		printf("Valor invalido...\n");
		printf("Retornando.\n\n");
		system("pause");
		goto inicio;
	}
	
	switch(op){
		case '1':{
			system("cls");
			printf("Vetores, Exercicio 4\n");
			
			for(int i=0;i<13;i++){
				printf("\nInsira o vetor[%i]: ",i);
				scanf("%i",&vet[i]);
			}
			
			goto iniciop;
			break;
		}
		case '2':{
			
			for(int i=0;i<13;i++){
				vet[i] = rand() % 1000;
			}
			
			for(int i=0; i<13; i++){
         	for(int a=0; a<13; a++){
             if(i == a)
                 continue;
             if(vet[i] == vet[i])
                 vet[a] = rand()%1000;
        		}
     		}
     		
			goto iniciop;
			break;
		}
}

iniciop:
	
	char xy,yx;
	
	system("cls");
	
	xy:
	printf("Vetores, Exercicio 4\n\n");
	
	printf("\nInsira o indice [0 - 12] que deseja ver o valor: ");
	scanf("%i",&x);
	
	if(x<0){
		printf("Insira um valor dentro do intervalo indicado.\n");
		system("pause");
		system("cls");
		goto xy;
	}
	
	if(x>12){
		printf("Insira um valor dentro do intervalo indicado.\n");
		system("pause");
		system("cls");
		goto xy;
	}
	
	yx:
	printf("\nInsira o indice que deseja ver o valor: ");
	scanf("%i",&y);
	
	if(y<0){
		printf("Insira um valor dentro do intervalo indicado.\n");
		system("pause");
		system("cls");
		printf("\n\n");
		goto yx;
	}
	
	if(y>12){
		printf("Insira um valor dentro do intervalo indicado.\n");
		system("pause");
		system("cls");
		printf("\n\n");
		goto yx;
	}
	
	system("cls");
	
	printf("Vetores, Exercicio 4\n\n");
	
	for(int i=0; i<13 ; i++){
		printf("O vetor[%i] é %i\n",i,vet[i]);
	}
	
	printf("\nOs indices selecionados tem o valor\n");
	printf("Vetor[%i] = %i, Vetor[%i] = %i\n\n",x,vet[x],y,vet[y]);
	
	printf("Aperte qualquer botão para retornar ou [N] para sair\n");
	op2=getche();
	op2=toupper(op2);
	
	if(op2 !='N'){
		goto inicio;
	}
	
	printf("\n");
	printf("Saindo...");
	
	exit(0);

}
