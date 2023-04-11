#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

int escolha_player,escolha_maquina;
char sair;

main(){
	setlocale(LC_ALL,"portuguese");
	srand(time(NULL));
	
			//Jogada do player
	do{
	
		do{
			system("cls");
			printf("Faça sua jogada\n1 - Pedra\n2 - Papel\n3 - Tesoura\n\n");
			printf("Insira sua jogada (1,2 ou 3): ");
			scanf("%i",&escolha_player);
			
			if(escolha_player > 3 || escolha_player < 0){
				printf("\n\nPor favor, insira um valor valido...\n\n");
				system("pause");
			}
			
		}while(escolha_player > 3 || escolha_player <= 0);
		
		system("cls");
		printf("Pedra, Papel ou Tesoura\n\n");
		
		escolha_maquina = rand() % 3+1;
		
		if(escolha_player == 1){
			
			if(escolha_maquina == 1){
				printf("Player [PEDRA] || MAQUINA [PEDRA] || EMPATE");
			}
			
			if(escolha_maquina == 2){
				printf("Player [PEDRA] || MAQUINA [PAPEL] || VITORIA DA MAQUINA");
			}
			
			if(escolha_maquina == 3){
				printf("Player [PEDRA] || MAQUINA [TESOURA] || VITORIA DO JOGADOR");
			}
			
		}
		
		else if(escolha_player == 2){
			
			if(escolha_maquina == 1){
				printf("Player [PAPEL] || MAQUINA [PEDRA] || VITORIA DO JOGADOR");
			}
			
			if(escolha_maquina == 2){
				printf("Player [PAPEL] || MAQUINA [PAPEL] || EMPATE");
			}
			
			if(escolha_maquina == 3){
				printf("Player [PAPEL] || MAQUINA [TESOURA] || VITORIA DA MAQUINA");
			}
		}
		else if(escolha_player == 3){
			
			if(escolha_maquina == 1){
				printf("Player [TESOURA] || MAQUINA [PEDRA] || VITORIA DA MAQUINA");
			}
			
			if(escolha_maquina == 2){
				printf("Player [TESOURA] || MAQUINA [PAPEL] || VITORIA DO PLAYER");
			}
			
			if(escolha_maquina == 3){
				printf("Player [TESOURA] || MAQUINA [TESOURA] || EMPATE");
			}
		}
		
		printf("\n\nDeseja jogar novamente? [N] para sair");
		sair = getche();
		sair = toupper(sair);
		
	}while(sair != 'N');

}
