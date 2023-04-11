#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<string.h>

int estoque[5][5]= {{150,0,100,150,200}, {200,300,230,100,90}, {250,300,0,200,150}, {300,100,90,450,0},{350,300,400,250,200}};
int armazem,produto,selecao,quantidadeAserModificada;
char inicio;

main(){
inicio:
	fflush (stdin);
	
	do{
		do{
			selecao = 0;
			quantidadeAserModificada = 0;
		
	setlocale(LC_ALL,"portuguese");
	system("cls");
	printf("Qual armazém você deseja manipular?\n\n");
	
	for(int i=0;i<5;i++){
		printf("\n\nArmazém: %i\n",i);
		for(int j=0;j<5;j++){
			printf("Produto (%i) : ",j);
			printf("%i || ",estoque[i][j]);
		}
	}
	
	printf("\n\n");
	printf("Insira Armazém e Produto: ");
	scanf("%i,%i",&armazem,produto);
	fflush(stdin);
	
	if(armazem > 4 || produto > 4 || armazem < 0 || produto < 0){
		system("cls");
		printf("Por favor coloque um valor valído\n\n");
		system("pause");
	}
	
}while(armazem > 4 || produto > 4 || armazem < 0 || produto < 0);

system("cls");
printf("Armazém: %i - Produto: %i\n\n",armazem,produto);

printf("O que deseja fazer?\n\n");
printf("Adicionar produtos ao estoque: (1)\n");
printf("Remover produtos do estoque: (2)\n");
printf("Retornar: (3)\n\n");

scanf("%i",&selecao);
fflush (stdin);

}while(selecao >= 3 || selecao < 0);

switch (selecao){
	case 1:{
			printf("\n\nArmazém: %i - Produto(%i) : %i || Insira a quantidade a ser adicionada: ",armazem,produto,estoque[armazem][produto]);
			scanf("%i",&quantidadeAserModificada);
			
			printf("Antigo estoque: %i\n\n",estoque[armazem][produto]);
			estoque[armazem][produto] = estoque[armazem][produto] + quantidadeAserModificada;
			printf("Novo estoque: %i\n\n",estoque[armazem][produto]);
			
			system("pause");
		
		break;
	}
	
	case 2:{
			printf("Armazém: %i - Produto(%i) : %i || Insira a quantidade a ser removida: ",armazem,produto,estoque[armazem][produto]);
			scanf("%i",&quantidadeAserModificada);
			
			if(quantidadeAserModificada > estoque[armazem][produto]){
				printf("\nEstoque insuficiente para suprir a demanda\n\n");
				
				quantidadeAserModificada == 0;
				system("pause");
			}
			
			if(quantidadeAserModificada == estoque[armazem][produto]){
				printf("\nEstoque zerado favor reabastecer\n\n");
				
				system("pause");	
			}
			
			printf("Antigo estoque: %i\n\n",estoque[armazem][produto]);
			estoque[armazem][produto] = estoque[armazem][produto] - quantidadeAserModificada;
			printf("Novo estoque: %i\n\n",estoque[armazem][produto]);
			
			system("pause");
			
		break;
	}
}

goto inicio;

}
