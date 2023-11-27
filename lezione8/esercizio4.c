//fai una funzione che prenda in input x,y e z e inserisca in z il risultato di x+y
#include <stdio.h>

void somma_insert(int x, int y, int *z){
	*z=x+y;
}

int main(){
	int x=2;
	int y=3;
	int z=0;
	somma_insert(x,y,&z);
	printf("z è: %d\n",z);
}
