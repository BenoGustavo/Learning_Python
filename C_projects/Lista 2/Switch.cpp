#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>

int op;

main(){

    printf("Insira o valor 1 ou 2");
    scanf("%i",&op);

    printf("%i",op);
    system("pause");

switch (op)
{
case 1:
    printf("1");
    break;

case 2:
printf("2");
break;

default:

printf("3++");
    break;
}
    return 0;
}
