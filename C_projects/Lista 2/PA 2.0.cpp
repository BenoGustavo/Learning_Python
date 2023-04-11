#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

float base,prog,pa,soma;
int x;
char op;

main(){

do{

system("cls");

    setlocale(LC_ALL,"portuguese");

    printf("Progressão artimetica\n\n");
        printf("Insira aqui o valor base e o valor da progressão, respectivamente: ");
        scanf("%f %f",&base ,&prog);
            printf("\nInsira a o valor ao qual você deseja saber: ");
             scanf("%i",&x);

             system("cls");
             printf("Progressão artimetica\n\n");

             pa=base;

             printf("O valor N[1] da PA é: %.2f\n\n",base);
        
        for (int i = 2; i < x+1; i++)
        {
            pa=pa+prog;

            printf("O valor N[%i] da PA é: %.2f\n",i,pa);

            soma=soma+pa;

            //teste do if else

             if(i==2){
                printf("                                                                                              Life goes\n");
            }else{
                printf("                                                                                              on and\n");
            }

            if (i==x)
            {
                soma=soma+base;
              printf("\n\nO ultimo da termo da sua PA é: %.2f",pa);
              printf("\n\nA soma da sua PA é: %.2f",soma);

            }
            

        }

        printf("\n\n");
        printf("Deseja calcular novamente? [S] OR [N]");
        op=getche();
        op=toupper(op);

}while (op != 'N');

printf("\nSaindo...");

        printf("\n\n");
}