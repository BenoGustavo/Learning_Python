/* 1 - Construa um programa em C/C++ que tenha as seguintes opções de Menu:
	
1.1 - Leia um vetor de 10 posições com valores aleatórios 0-100 e na
sequência selecione aleatoriamente três posições/índices deste vetor e
apresente os seus valores e a multiplicação destes.

1.2 - Leia dois vetores de 5 posições com valores inteiros cada e gere um
terceiro com os resultados da soma dos valores sendo a lógica: soma o 1a
elemento do 1o vetor com o 5o elemento do 2o vetor, 2a elemento do 1o vetor
com o 4o elemento do 2o vetor, e assim sucessivamente.

1.3 - Construa um vetor de 13 posições com valores caracteres aleatórios e na
sequência pedir para o usuário digitar um caractere e localizar onde este está
no vetor e quantas vezes aparece. */

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

char slc,menu;

main(){
	setlocale(LC_ALL,"portuguese");
	menu:
		system("cls");
		
	printf("Vetores exercicio - 1\n\n");
	printf("1 - Ler 1 vetor com 10 caracteres aleatorios de 0 a 100, e multiplicalos entre sí\n\n");
	printf("2 - Ler 2 vetores inteiros com 5 caracteres e somalos dentro de um padrão\n\n");
	printf("3 - Ler 1 vetor com 13 caracteres aleatorios, e pedir pra o usuario chutar um valor que possa existir dentro do mesmo\n\n");
	printf("4 - Sair\n");
	slc=getche();
	
	if(slc>'4'){
		printf("Comando invalido, retornando...\n\n");
		system("pause");
		goto menu;
	}
	
	switch(slc){
		case '1':{
			system("cls");
			int vet[10],x,y,z,res;
			
			printf("Vetor com 10 caracteres de 0 a 100\n\n");
			
			for(int i=0; i<10 ;i++){
				fflush(stdin);	
			vet[i] = rand() % 101;
		}
		
			for(int i=0; i<10 ;i++)	{
				fflush(stdin);
			printf("Vetor %i: %i \n",i,vet[i]);
		}
			printf("\nMultiplicando...\n\n");
			
			x = rand() % 10 ; y = rand() % 10 ; z = rand() % 10 ;
			
				fflush(stdin);
			
			res = vet[x] * vet[y] * vet[z];
			
				fflush(stdin);
				
			printf("O vetor[%i] * O vetor [%i] * O vetor [%i]\n\n",x,y,z);
			printf("Ou seja %i, %i, %i tem como ",vet[x],vet[y],vet[z]);
			printf("resultado: %i\n\n",res);
			
			system("pause");
			
			goto menu;
			
			break;
		}
		case '2':{
			system("cls");
			
			int vet2[5],vet3[5],res2,aux;
			
			printf("2 vetores 5 caracteres e soma\n\n");
			for(int i=0; i<5 ; i++){
				printf("\nInsira o Vetor[%i]: ",i);
				scanf("%i",&vet2[i]);
			}
			for(int i=0; i<5 ; i++){
				printf("\nInsira o Vetor[%i]: ",i);
				scanf("%i",&vet3[i]);
			}
			
			system("cls");
			
			printf(" 2 vetores 5 caracteres e soma \n\n");
			
			for(int i=0; i<5 ; i++){
				printf("Vetor 1 [%i] é %i // Vetor 2 [%i] é %i\n",i,vet2[i],i,vet3[i]);
			}
			
			aux=5;
			
			for(int i=0; i<5 ; i++){
				aux=aux-1;
				
				res2 = vet2[i] + vet3[aux];
				printf("\nVetor 1 [%i] + Vetor 2 [%i] = %i\n",vet2[i],vet3[aux],res2);
				
			}
			
			printf("\n\n");
			system("pause");
			
			goto menu;
			break;
		}
		
		case'3':{
			system("cls");
			int vet3[12],chute,indice,erro,m50;
			
			m50:
			
			erro=0;
			
			printf("Acerte se puder...\n");
			printf("Chance de acerto de 1 em 50\n\n");
			printf("Insira o seu chute [1-50]: ");
			scanf("%i",&chute);
			
			if(chute>50){
				system("cls");
				printf("Acerte se puder...\n\n");
				printf("Por favor coloque um número dentro do intervalo de [1-50]\n\n");
				printf("Retornando...\n\n");
				
				system("pause");
				system("cls");
				goto m50;
			}
			
			for(int i=0;i<13;i++){
				vet3[i] = rand() % 51;
			}
			
			//Codigo para não repetir números dentro do rand.
			
     for(int i=0; i<13; i++){
         for(int a=0; a<13; a++){
             if(i == a)
                 continue;
             if(vet3[i] == vet3[i])
                 vet3[a] = rand()%51 + 1;
         }
     }
			
			for(int i=0;i<13;i++){
				if(vet3[i]==chute){
					erro=1;
					indice=i;
				}
			}
			
			if(erro !=1){
				
				for(int i=0;i<13;i++){
					printf("%i - Vetor [%i]\n",i,vet3[i]);
				}
				
				printf("\nVocê errou, o valor [%i] não existe dentro do vetor\n\n",chute);
				
				system("pause");
				
				goto menu;
			}
			
			for(int i=0;i<13;i++){
				printf("Vetor %i = [%i]\n",i,vet3[i]);
			}
			
			printf("\nParabéns, voce acertou\n");
			printf("O vetor[%i] de valor [%i] tem o mesmo valor do seu chute [%i]\n\n",indice,vet3[indice],chute);
			
			system("pause");
			goto menu;
			break;
		}
		default:{
			system("cls");
			printf("Saindo...");
			exit(0);
			break;
		}
	}
} 
