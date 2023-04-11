#include<conio.h> 
#include<stdio.h> 
#include<iostream>
#include<locale.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

int vet[5],q;
char vetEx[5][3],op,inicio,menu;

main(){
	setlocale(LC_ALL,"portuguese");
	
	menu:
	
	printf("Vetores - Exercicio 13\n\n");
	srand(time(NULL));
	
	printf("Menu:\n");
	printf("1 - Aleatorizar vetor\n");
	printf("2 - Inserir manualmente \n");
	op=getche();
	
	switch(op){
		case '1':{
			system("cls");
				printf("Vetores - Exercicio 13\n\n");
				
				for(int i=0;i<5;i++){
		
				vet[i]= rand() %201;
		
				printf("Vetor[%i] =  %i \n",i,vet[i]);
		
				itoa(vet[i],vetEx[i],10);
		
				printf("Valor transformado em string = %s \n\n", vetEx[i]);
	}
	
	goto inicio;
			break;
		}
		case '2':{
			
				system("cls");
				printf("Vetores - Exercicio 13\n");
				
				for(int i=0;i<5;i++){
					printf("\nInsira um valor de (0 - 201) o vetor[%i]: ",i);
					scanf("%i",&vet[i]);
					
					if(vet[i]>200 || vet[i]<0){
						printf("\n\nValor fora do intervalo selecionado\n\n");
						i=i-1;
					}
					
					itoa(vet[i],vetEx[i],10);
				}
				
				system("cls");
				printf("Vetores - Exercicio 13\n");
				
				for(int i=0;i<5;i++){
					printf("\nVetor[%i] = %i\n",i,vet[i]);
				}
		goto inicio;
			break;
		}
		
		default:{
			system("cls");
			goto menu;
			break;
		}
	}
	
	inicio:
	
	for(int i=0;i<5;i++){
		
		q=strlen(vetEx[i]); //strlen com problema...
		if(q>=3 && vet[i] == 200){
			if(vetEx[i][0]=='1'){
				printf("\nDuzentos");
			}
		}
		
		if(q>=3 && vet[i] == 100){
			if(vetEx[i][0]=='1'){
				printf("\nCem");
			}
		}
		
		if(q>=3 && vet[i] >100){
				
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '1' && vetEx[i][2]== '0' ){
	 	 	printf("\nCento e Dez");
			  }
	 	  
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '1' && vetEx[i][2]== '1' ){
	 	 	printf("\nCento e Onze");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '1' && vetEx[i][2]== '2' ){
	 	 	printf("\nCento e Doze");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '1' && vetEx[i][2]== '3' ){
	 	 	printf("\nCento e Treze");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '1' && vetEx[i][2]== '4' ){
	 	 	printf("\nCento e Quatorze");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '1' && vetEx[i][2]== '5' ){
	 	 	printf("\nCento e Quinze");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '1' && vetEx[i][2]== '6' ){
	 	 	printf("\nCento e Dezesseis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '1' && vetEx[i][2]== '7' ){
	 	 	printf("\nCento e Dezessete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '1' && vetEx[i][2]== '8' ){
	 	 	printf("\nCento e Dezoito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '1' && vetEx[i][2]== '9' ){
	 	 	printf("\nCento e Dezenove");
			  }
		if(vetEx[i][0]== '1' && vetEx[i][1]== '2'){
	 	 	printf("\nCento e vinte");
			  }
	 	  
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '2' && vetEx[i][2]== '1' ){
	 	 	printf(" e um");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '2' && vetEx[i][2]== '2' ){
	 	 	printf(" e dois");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '2' && vetEx[i][2]== '3' ){
	 	 	printf(" e tres");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '2' && vetEx[i][2]== '4' ){
	 	 	printf(" e quatro");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '2' && vetEx[i][2]== '5' ){
	 	 	printf(" e cinco");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '2' && vetEx[i][2]== '6' ){
	 	 	printf(" e seis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '2' && vetEx[i][2]== '7' ){
	 	 	printf(" e sete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '2' && vetEx[i][2]== '8' ){
	 	 	printf(" e oito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '2' && vetEx[i][2]== '9' ){
	 	 	printf(" e nove");
			  }
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '3'){
	 	 	printf("\nCento e trinta");
			  }
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '3' && vetEx[i][2]== '1' ){
	 	 	printf(" e um");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '3' && vetEx[i][2]== '2' ){
	 	 	printf(" e dois");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '3' && vetEx[i][2]== '3' ){
	 	 	printf(" e tres");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '3' && vetEx[i][2]== '4' ){
	 	 	printf(" e quatro");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '3' && vetEx[i][2]== '5' ){
	 	 	printf(" e cinco");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '3' && vetEx[i][2]== '6' ){
	 	 	printf(" e seis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '3' && vetEx[i][2]== '7' ){
	 	 	printf(" e sete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '3' && vetEx[i][2]== '8' ){
	 	 	printf(" e oito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '3' && vetEx[i][2]== '9' ){
	 	 	printf(" e nove");
			  }
		}
		
		if(vetEx[i][0]== '1' && vetEx[i][1]== '4'){
	 	 	printf("\nCento e quarenta");
			  }
		if(vetEx[i][0]== '1' && vetEx[i][1]== '4' && vetEx[i][2]== '1' ){
	 	 	printf(" e um");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '4' && vetEx[i][2]== '2' ){
	 	 	printf(" e dois");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '4' && vetEx[i][2]== '3' ){
	 	 	printf(" e tres");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '4' && vetEx[i][2]== '4' ){
	 	 	printf(" e quatro");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '4' && vetEx[i][2]== '5' ){
	 	 	printf(" e cinco");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '4' && vetEx[i][2]== '6' ){
	 	 	printf(" e seis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '4' && vetEx[i][2]== '7' ){
	 	 	printf(" e sete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '4' && vetEx[i][2]== '8' ){
	 	 	printf(" e oito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '4' && vetEx[i][2]== '9' ){
	 	 	printf(" e nove");
			  }
		
		if(vetEx[i][0]== '1' && vetEx[i][1]== '5'){
	 	 	printf("\nCento e cinquenta");
			  }
				if(vetEx[i][0]== '1' && vetEx[i][1]== '5' && vetEx[i][2]== '1' ){
	 	 	printf(" e um");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '5' && vetEx[i][2]== '2' ){
	 	 	printf(" e dois");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '5' && vetEx[i][2]== '3' ){
	 	 	printf(" e tres");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '5' && vetEx[i][2]== '4' ){
	 	 	printf(" e quatro");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '5' && vetEx[i][2]== '5' ){
	 	 	printf(" e cinco");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '5' && vetEx[i][2]== '6' ){
	 	 	printf(" e seis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '5' && vetEx[i][2]== '7' ){
	 	 	printf(" e sete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '5' && vetEx[i][2]== '8' ){
	 	 	printf(" e oito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '5' && vetEx[i][2]== '9' ){
	 	 	printf(" e nove");
			  }
				if(vetEx[i][0]== '1' && vetEx[i][1]== '6'){
	 	 	printf("\nCento e sessenta");
			  }
				if(vetEx[i][0]== '1' && vetEx[i][1]== '6' && vetEx[i][2]== '1' ){
	 	 	printf(" e um");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '6' && vetEx[i][2]== '2' ){
	 	 	printf(" e dois");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '6' && vetEx[i][2]== '3' ){
	 	 	printf(" e tres");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '6' && vetEx[i][2]== '4' ){
	 	 	printf(" e quatro");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '6' && vetEx[i][2]== '5' ){
	 	 	printf(" e cinco");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '6' && vetEx[i][2]== '6' ){
	 	 	printf(" e seis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '6' && vetEx[i][2]== '7' ){
	 	 	printf(" e sete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '6' && vetEx[i][2]== '8' ){
	 	 	printf(" e oito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '6' && vetEx[i][2]== '9' ){
	 	 	printf(" e nove");
			  }
				if(vetEx[i][0]== '1' && vetEx[i][1]== '7'){
	 	 	printf("\nCento e setenta");
			  }
				if(vetEx[i][0]== '1' && vetEx[i][1]== '7' && vetEx[i][2]== '1' ){
	 	 	printf(" e um");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '7' && vetEx[i][2]== '2' ){
	 	 	printf(" e dois");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '7' && vetEx[i][2]== '3' ){
	 	 	printf(" e tres");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '7' && vetEx[i][2]== '4' ){
	 	 	printf(" e quatro");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '7' && vetEx[i][2]== '5' ){
	 	 	printf(" e cinco");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '7' && vetEx[i][2]== '6' ){
	 	 	printf(" e seis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '7' && vetEx[i][2]== '7' ){
	 	 	printf(" e sete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '7' && vetEx[i][2]== '8' ){
	 	 	printf(" e oito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '7' && vetEx[i][2]== '9' ){
	 	 	printf(" e nove");
			  }
				if(vetEx[i][0]== '1' && vetEx[i][1]== '8'){
	 	 	printf("\nCento e oitenta");
			  }
				if(vetEx[i][0]== '1' && vetEx[i][1]== '8' && vetEx[i][2]== '1' ){
	 	 	printf(" e um");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '8' && vetEx[i][2]== '2' ){
	 	 	printf(" e dois");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '8' && vetEx[i][2]== '3' ){
	 	 	printf(" e tres");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '8' && vetEx[i][2]== '4' ){
	 	 	printf(" e quatro");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '8' && vetEx[i][2]== '5' ){
	 	 	printf(" e cinco");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '8' && vetEx[i][2]== '6' ){
	 	 	printf(" e seis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '8' && vetEx[i][2]== '7' ){
	 	 	printf(" e sete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '8' && vetEx[i][2]== '8' ){
	 	 	printf(" e oito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '8' && vetEx[i][2]== '9' ){
	 	 	printf(" e nove");
			  }
				if(vetEx[i][0]== '1' && vetEx[i][1]== '9'){
	 	 	printf("\nCento e noventa");
			  }
				if(vetEx[i][0]== '1' && vetEx[i][1]== '9' && vetEx[i][2]== '1' ){
	 	 	printf(" e um");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '9' && vetEx[i][2]== '2' ){
	 	 	printf(" e dois");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '9' && vetEx[i][2]== '3' ){
	 	 	printf(" e tres");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '9' && vetEx[i][2]== '4' ){
	 	 	printf(" e quatro");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '9' && vetEx[i][2]== '5' ){
	 	 	printf(" e cinco");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '9' && vetEx[i][2]== '6' ){
	 	 	printf(" e seis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '9' && vetEx[i][2]== '7' ){
	 	 	printf(" e sete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '9' && vetEx[i][2]== '8' ){
	 	 	printf(" e oito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '9' && vetEx[i][2]== '9' ){
	 	 	printf(" e nove");
			  }
			  				if(vetEx[i][0]== '1' && vetEx[i][1]== '0'){
	 	 	printf("\nCento");
			  }
				if(vetEx[i][0]== '1' && vetEx[i][1]== '0' && vetEx[i][2]== '1' ){
	 	 	printf(" e um");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '0' && vetEx[i][2]== '2' ){
	 	 	printf(" e dois");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '0' && vetEx[i][2]== '3' ){
	 	 	printf(" e tres");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '0' && vetEx[i][2]== '4' ){
	 	 	printf(" e quatro");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '0' && vetEx[i][2]== '5' ){
	 	 	printf(" e cinco");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '0' && vetEx[i][2]== '6' ){
	 	 	printf(" e seis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '0' && vetEx[i][2]== '7' ){
	 	 	printf(" e sete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '0' && vetEx[i][2]== '8' ){
	 	 	printf(" e oito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '0' && vetEx[i][2]== '9' ){
	 	 	printf(" e nove");
			  }		
		
		if(q==2 && vet[i] > 9){

		if(vetEx[i][0]== '1' && vetEx[i][1]== '0' ){
	 	 	printf("\n Dez");
			  }
	 	  
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '1' ){
	 	 	printf("\n Onze");
			  }
	 	
		 if(vetEx[i][0]== '1' && vetEx[i][1]== '2' ){
	 	 	printf("\n Doze");
			  } 
	 	 
		  if(vetEx[i][0]== '1' && vetEx[i][1]== '3' ){
	 	 	printf("\n Treze");
			  }
			  	
	 	if(vetEx[i][0]== '1' && vetEx[i][1]== '4' ){
	 	 	printf("\n Quatorze");
			  } 	
	 	 	
	      if(vetEx[i][0]== '1' && vetEx[i][1]== '5' ){
	 	 	printf("\n Quinze");
			  }	 
			  
		if(vetEx[i][0]== '1' && vetEx[i][1]== '6' ){
	 	 	printf("\n Dezesseis");
			  }	  	
	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '7' ){
	 	 	printf("\n Dezessete");
			  } 
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '8' ){
	 	 	printf("\n Dezoito");
			  }
	 	 	
		if(vetEx[i][0]== '1' && vetEx[i][1]== '9' ){
	 	 	printf("\n Dezenove");
			  }
		}
		
		if(q==2 && vet[i] > 19){
		
		if(vetEx[i][0]== '2'){
	 	 	printf("\n Vinte");
	 	 	if(vetEx[i][1] >0 ){
	 	 		if(vetEx[i][1]== '1'){
	 	 			printf(" e um");
				  }
				  if(vetEx[i][1]== '2'){
				  	printf(" e dois");
				  }
				  if(vetEx[i][1]== '3'){
				  	printf(" e três");
				  }
				  if(vetEx[i][1]== '4'){
				  	printf(" e quatro");
				  }
				  if(vetEx[i][1]== '5'){
				  	printf(" e cinco");
			      }
				  if(vetEx[i][1]== '6'){
				  	printf(" e seis");
				  }
				  if(vetEx[i][1]== '7'){
				  	printf(" e sete");
				  }
				  if(vetEx[i][1]== '8'){
				  	printf(" e oito");
				  }
				  if(vetEx[i][1]== '9'){
				  	printf(" e nove");
				}
					}
			}
			if(vetEx[i][0]== '3'){
				printf("\n Trinta");
				if(vetEx[i][1] >0 ){
	 	 		if(vetEx[i][1]== '1'){
	 	 			printf(" e um");
				  }
				  if(vetEx[i][1]== '2'){
				  	printf(" e dois");
				  }
				  if(vetEx[i][1]== '3'){
				  	printf(" e três");
				  }
				  if(vetEx[i][1]== '4'){
				  	printf(" e quatro");
				  }
				  if(vetEx[i][1]== '5'){
				  	printf(" e cinco");
			      }
				  if(vetEx[i][1]== '6'){
				  	printf(" e seis");
				  }
				  if(vetEx[i][1]== '7'){
				  	printf(" e sete");
				  }
				  if(vetEx[i][1]== '8'){
				  	printf(" e oito");
				  }
				  if(vetEx[i][1]== '9'){
				  	printf(" e nove");
				}
					}
		}
		if(vetEx[i][0]== '4'){
				printf("\n Quarenta");
					if(vetEx[i][1] >0 ){
	 	 		if(vetEx[i][1]== '1'){
	 	 			printf(" e um");
				  }
				  if(vetEx[i][1]== '2'){
				  	printf(" e dois");
				  }
				  if(vetEx[i][1]== '3'){
				  	printf(" e três");
				  }
				  if(vetEx[i][1]== '4'){
				  	printf(" e quatro");
				  }
				  if(vetEx[i][1]== '5'){
				  	printf(" e cinco");
			      }
				  if(vetEx[i][1]== '6'){
				  	printf(" e seis");
				  }
				  if(vetEx[i][1]== '7'){
				  	printf(" e sete");
				  }
				  if(vetEx[i][1]== '8'){
				  	printf(" e oito");
				  }
				  if(vetEx[i][1]== '9'){
				  	printf(" e nove");
				}
					}
			}
			if(vetEx[i][0]== '5'){
				printf("\n Cinquenta");
						if(vetEx[i][1] >0 ){
	 	 		if(vetEx[i][1]== '1'){
	 	 			printf(" e um");
				  }
				  if(vetEx[i][1]== '2'){
				  	printf(" e dois");
				  }
				  if(vetEx[i][1]== '3'){
				  	printf(" e três");
				  }
				  if(vetEx[i][1]== '4'){
				  	printf(" e quatro");
				  }
				  if(vetEx[i][1]== '5'){
				  	printf(" e cinco");
			      }
				  if(vetEx[i][1]== '6'){
				  	printf(" e seis");
				  }
				  if(vetEx[i][1]== '7'){
				  	printf(" e sete");
				  }
				  if(vetEx[i][1]== '8'){
				  	printf(" e oito");
				  }
				  if(vetEx[i][1]== '9'){
				  	printf(" e nove");
				}
					}
			}
			if(vetEx[i][0]== '6'){
				printf("\n Sessenta");
				if(vetEx[i][1] >0 ){
	 	 		if(vetEx[i][1]== '1'){
	 	 			printf(" e um");
				  }
				  if(vetEx[i][1]== '2'){
				  	printf(" e dois");
				  }
				  if(vetEx[i][1]== '3'){
				  	printf(" e três");
				  }
				  if(vetEx[i][1]== '4'){
				  	printf(" e quatro");
				  }
				  if(vetEx[i][1]== '5'){
				  	printf(" e cinco");
			      }
				  if(vetEx[i][1]== '6'){
				  	printf(" e seis");
				  }
				  if(vetEx[i][1]== '7'){
				  	printf(" e sete");
				  }
				  if(vetEx[i][1]== '8'){
				  	printf(" e oito");
				  }
				  if(vetEx[i][1]== '9'){
				  	printf(" e nove");
				}
					}
			}
			if(vetEx[i][0]== '7'){
				printf("\n Setenta");
				if(vetEx[i][1] >0 ){
	 	 		if(vetEx[i][1]== '1'){
	 	 			printf(" e um");
				  }
				  if(vetEx[i][1]== '2'){
				  	printf(" e dois");
				  }
				  if(vetEx[i][1]== '3'){
				  	printf(" e três");
				  }
				  if(vetEx[i][1]== '4'){
				  	printf(" e quatro");
				  }
				  if(vetEx[i][1]== '5'){
				  	printf(" e cinco");
			      }
				  if(vetEx[i][1]== '6'){
				  	printf(" e seis");
				  }
				  if(vetEx[i][1]== '7'){
				  	printf(" e sete");
				  }
				  if(vetEx[i][1]== '8'){
				  	printf(" e oito");
				  }
				  if(vetEx[i][1]== '9'){
				  	printf(" e nove");
				}
					}
			}
			if(vetEx[i][0]== '8'){
				printf("\n Ointenta");
				if(vetEx[i][1] >0 ){
	 	 		if(vetEx[i][1]== '1'){
	 	 			printf(" e um");
				  }
				  if(vetEx[i][1]== '2'){
				  	printf(" e dois");
				  }
				  if(vetEx[i][1]== '3'){
				  	printf(" e três");
				  }
				  if(vetEx[i][1]== '4'){
				  	printf(" e quatro");
				  }
				  if(vetEx[i][1]== '5'){
				  	printf(" e cinco");
			      }
				  if(vetEx[i][1]== '6'){
				  	printf(" e seis");
				  }
				  if(vetEx[i][1]== '7'){
				  	printf(" e sete");
				  }
				  if(vetEx[i][1]== '8'){
				  	printf(" e oito");
				  }
				  if(vetEx[i][1]== '9'){
				  	printf(" e nove");
				}
					}
	}
				if(vetEx[i][0]== '9'){
				printf("\n noventa");
					if(vetEx[i][1] >0 ){
	 	 		if(vetEx[i][1]== '1'){
	 	 			printf(" e um");
				  }
				  if(vetEx[i][1]== '2'){
				  	printf(" e dois");
				  }
				  if(vetEx[i][1]== '3'){
				  	printf(" e três");
				  }
				  if(vetEx[i][1]== '4'){
				  	printf(" e quatro");
				  }
				  if(vetEx[i][1]== '5'){
				  	printf(" e cinco");
			      }
				  if(vetEx[i][1]== '6'){
				  	printf(" e seis");
				  }
				  if(vetEx[i][1]== '7'){
				  	printf(" e sete");
				  }
				  if(vetEx[i][1]== '8'){
				  	printf(" e oito");
				  }
				  if(vetEx[i][1]== '9'){
				  	printf(" e nove");
				}
					}
			}
		}
			if(q==1){
		if(vetEx[i][0]== '0'){
	 	 	printf("\n Zero");}
	 	if(vetEx[i][0]== '1'){
	 	 	printf("\n Um");} 	
        if(vetEx[i][0]== '2'){
	 	 	printf("\n Dois");}
	 	if(vetEx[i][0]== '3'){
	 	 	printf("\n Três");}
		if(vetEx[i][0]== '4'){
	 	 	printf("\n Quatro");}
		if(vetEx[i][0]== '5'){
	 	 	printf("\n Cinco");}	  	   	
	 	if(vetEx[i][0]== '6'){
	 	 	printf("\n Seis");} 	
	 	if(vetEx[i][0]== '7'){
	 	 	printf("\n Sete");}
		if(vetEx[i][0]== '8'){
	 	 	printf("\n Oito");}	 
		if(vetEx[i][0]== '9'){
	 	 	printf("\n Nove");}	 
			}
		
		}
	
	printf("\n\n");
	printf("Aperte qualquer tecla para retornar ou 'N' para sair\n");
	op=getche();
	op=toupper(op);
	
	if(op=='N'){
		exit(0);
	}else{
		system("cls");
		goto menu;
	}
	
	}

