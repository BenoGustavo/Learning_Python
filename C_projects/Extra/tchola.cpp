//2. Fazer um programa em C que imprime uma tabela com a tabuada de 1 a 9

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

int num1,num2,num3,num4,num5,num6,num7,num8,num9;
int res,res1,res2,res3,res4,res5,res6,res7,res8,res9;
char op;

main(){
	setlocale(LC_ALL,"portuguese");
	
	do{
		
		system("cls");
	
	printf("Tabuada de 9 num, automatico\n\n");
	printf("Insira [3] valores inteiros: ");
		scanf("%i %i %i",&num1,&num2,&num3);
	printf("\nInsira [3] valores inteiros: ");
		scanf("%i %i %i",&num4,&num5,&num6);
	printf("\nInsira [3] valores inteiros: ");
		scanf("%i %i %i",&num7,&num8,&num9);
		printf("\n");
		system("cls");
		printf("Tabuada de 9 num, automatico\n\n");
		for(int i=1; i<10; i++){
			
			
			{
			res=1*i;
			
			res1=num1*i;
			
			res2=num2*i;
			
			res3=num3*i;
			
			res4=num4*i;
			
			res5=num5*i;
			
			res6=num6*i;
			
			res7=num7*i;
			
			res8=num8*i;
			
			res9=num9*i;
		}
			printf("%i - %i %i %i %i %i %i %i %i %i \n",res,res1,res2,res3,res4,res5,res6,res7,res8,res9);
			printf("\n");
		}
		
		printf("Digite [S] para retornar ou [N] para sair\n");
		op=getche();
		op=toupper(op);
		printf("Saindo...");
		}while(op != 'N');
		
		
		
		printf("\n\n");
		system("pause");
}
