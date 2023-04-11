#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<string.h>

char X,string[100];

int main(){
    setlocale(LC_ALL,"portuguese");
    printf("Insira sua frase: ");
    scanf("%[^\n]s",&string);
    
    printf("\nA letra que deseja saber a quantidade: ");
    scanf("%s",&X);
    
    X = toupper(X);
    
    int Quantidade_De_Caracteres = strlen(string);
    
        for(int i=0;i<Quantidade_De_Caracteres;i++){
    	string[i] = toupper(string[i]);	
	}
	
    int contador;
    
    for(int i=0;i<Quantidade_De_Caracteres;i++){
        if(X == string[i]){
            contador++;
            printf("\nLetra (%c) encontrada no indice (%i)\n",X,i+1);
        }
    }
    
    printf("\nDentro da frase (%s) a letra (%c) repete (%i) vezes",string,X,contador);
    
}

