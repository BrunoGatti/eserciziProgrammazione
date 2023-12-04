#include <stdio.h>
#include <stdlib.h>

int * array_di_uno(int* array, int dimensione_array){
	int somma=0;
	int * uni;
	for (int i=0;i< dimensione_array;i++){
		somma+=array[i];
	}
	//a questo punto somma contiene il valore di tutti gli elementi dell'array sommati, nel nostro esempio era 8

	//adesso voglio fare un array nuovo di 8 uni
	uni= malloc(sizeof(int)*somma);

	//una volta allocato l'array lo riempio di uni
	for (int i=0;i<dimensione_array;i++){
		uni[i]=1;
	}
	return uni;
}

int main(){
	int a[3]={1,2,3};
	int *b=NULL;
	b=array_di_uno(a,3);
	printf("Array di uni:[ ");

	for(int i=0;i<sizeof(b)/sizeof(int);i++){
		printf("%d,",b[i]);
	}

	printf("]\n");
}
