/*12. Leia um vetor de 13 posições contendo letras minúsculas, e na sequência
mostre o vetor original, o vetor com as letras em maiúscula. Após apresente
cada letra do vetor das minúsculas com o seu valor da tabela ASCII sendo o
decimal, Hexadecimal e Binário. E assim também para o vetor das Maiúsculas. rand 0 - 127 */

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

int vet[12];
char inicio,op;

int maior = 123, menor = 97;

//função que transforma em 1 ou 0
char bitsMin[13][9],bitsMaisc[13][9],c;
#define getbit(by, pos)  ((by >> pos)&0x1)

void byte2bits(char c, char* s)
{
    int i = 7;
    while(i >= 0)
        *s++ = '0' + getbit(c, i--);
    *s = 0;
}

main(){
	setlocale(LC_ALL,"portuguese");
	
	inicio:
		system("cls");
	
	printf("Vetores - Exercicio 12\n\n");
	
	for(int i=0;i<13;i++){
		vet[i] = menor + (rand() % (maior-menor));
	}
	
	for(int i=0; i<13; i++){
    for(int a=0; a<13; a++){
    if(i == a)
    continue;
    if(vet[i] == vet[i])
    vet[a] = menor + (rand() % (maior-menor));;
       	}
   	}
   	
   	printf("Minúsculas:\n\n");
   	
   	for(int i=0;i<13;i++){
   		char itoa(vet[i]);
	   }
	   
//conversão para binario
	for(int i=0;i<13;i++){
   		byte2bits(vet[i], bitsMin[i]);
   		}

//final
   	
	for(int i=0;i<13;i++){
   		printf("Vetor Original [%i] - [%i] Decimal / [%c] Caractere / [U+00%X] Hexadecimal / [%s] Binário \n",i,vet[i],vet[i],vet[i],bitsMin[i]);
	}
	
	printf("\nMaiúscula:\n\n");
	
	for(int i=0;i<13;i++){
		vet[i]=toupper(vet[i]);
		
		byte2bits(vet[i], bitsMaisc[i]);
		
   		printf("Vetor Original [%i] - [%i] Decimal / [%c] Caractere / [U+00%X] Hexadecimal / [%s] Binário \n",i,vet[i],vet[i],vet[i],bitsMaisc[i]);
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
