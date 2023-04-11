/*10. Leia dois vetores de 20 posições e calcule um outro vetor contendo, nas
posições pares os valores do primeiro e nas posições impares os valores do
segundo.*/

#include<cmath>
#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<math.h>
#include<stdlib.h>

char inicio,op;
int q=0;

main(){
	setlocale(LC_ALL,"portuguese");
	
	inicio:
		system("cls");
	
	printf("Vetores - Exercicio 10\n\n");
	printf("Insira a quantidade de indices desejada: ");
	scanf("%i",&q);
	
	int vetPar[q],vetImp[q],vetFinal[q]; //Vetores setados depois do main por conta do valor q, que necessita de uma variavel
	
	for(int i=0;i<q;i++){
		vetPar[i]=rand()% q+q;
		vetImp[i]=rand()% q+q;
	}
	
	for(int i=0; i<q; i++){
        for(int a=0; a<q; a++){
         if(i == a)
          continue;
          if(vetPar[i] == vetPar[i])
             vetPar[a] = rand()%q+q;
       	}
   	}
   	
   	for(int i=0; i<q; i++){
        for(int a=0; a<q; a++){
         if(i == a)
          continue;
          if(vetImp[i] == vetImp[i])
             vetImp[a] = rand()%q+q;
       	}
   	}
   	
   	for(int i=0;i<q;i++){
   		if(i % 2 == 0){
   			vetFinal[i]=vetPar[i];
		   }else{
		   	vetFinal[i]=vetImp[i];
		   }
	}
	
	// TELA
	
	system("cls");
	printf("Vetores - Exercicio 10\n\n");
	
	printf("Vetor Par e Vetor Impares:\n\n");
	for(int i=0;i<q;i++){
		printf("Vetor pares [%i] = %i  -  Vetor impares[%i] = %i\n",i,vetPar[i],i,vetImp[i]);
	}
	
	printf("\nVetor Final:\n\n");
	for(int i=0;i<q;i++){
		printf("Vetor[%i] = %i\n",i,vetFinal[i]);
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
