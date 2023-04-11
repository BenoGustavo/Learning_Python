/*33. Faça um algoritmo que calcule e mostre a área de um trapézio. Sabe-se que: A = (base
maior + base menor) * altura) /2;*/

#include<conio.h>
#include<stdio.h>
#include<iostream>
#include<locale.h>
#include<math.h>

float basemaior, basemenor, alt, area;

main(){
	setlocale(LC_ALL,"portuguese");
	printf("Area do trapezio\n\n");
	printf("Insira aqui a base menor e base maior do trapezio em cm: ");
	scanf("%f %f",&basemaior,& basemenor);
	printf("Insira aqui a altura do trapezio em cm: ");
	scanf("%f",&alt);
	
	area=(((basemaior*basemenor)*alt)/2);
	
	system("cls");
		printf("Area do trapezio\n\n");
			printf("Area do trapezio é %.2fcm",area);
			
			printf("\n\n");
			system("pause");
}
