//fai una funzione che prende un array in input e sputa in output la somma dei suoi elementi
#include<stdio.h>

int somma_elementi_array(int * array, int dimensione_array){
	int somma=0;
	for (int i=0;i<dimensione_array;i++){
		somma+=array[i];
	}
	return somma;
}

int main(){
    int	a[3]={1,3,5};

	printf("%d",somma_elementi_array(a,3));
}
