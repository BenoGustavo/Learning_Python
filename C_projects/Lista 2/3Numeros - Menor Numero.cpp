//faça o usuário digitar 3 valores entre 0 > e <10, e faça o código achar o menor numero digitado e motrar na tela.

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

float x,y,z;
char op;

main(){
    setlocale(LC_ALL,"portuguese");

    do{
        do{

    system("cls");
        printf("3 Números - Menor número, 1 à 9\n\n");

        printf("Digite o primeiro número[1] de 1 à 9: ");
             scanf("%f",&x);
        printf("\nDigite o primeiro número[2] de 1 à 9: ");
             scanf("%f",&y);
        printf("\nDigite o primeiro número[3] de 1 à 9: ");
             scanf("%f",&z);

            system("cls");

            if (x==0 || y==0 || z==0)
            {
                 printf("3 Números - Menor número, 1 à 9\n\n");
                 printf("Favor inserir um comando valido, retornando.\n");
                 system("pause");
            }
            }while (x==0 || y==0 || z==0);
            
            

             printf("3 Números - Menor número, 1 à 9\n\n");

    if((x<y)&&(x<z)){
       printf("O primeiro valor é o menor valor: %.2f\n",x);
    }
    if((y<x)&&(y<z)){
       printf("O segundo valor é o menor valor: %.2f\n",y);
    }
    if((z<x)&&(z<y)){
       printf("O terceiro valor é o menor valor: %.2f\n",z);
    }

printf("\nDeseja fazer novamente? [S] OR [N]");
op=getche();
op=toupper(op);

}while (op != 'N');

    
}