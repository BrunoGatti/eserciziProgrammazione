#include <stdio.h>

int main(){
	int x =3;
	int *y= &x;
	printf("indirizzo: %d, valore %d", y, *y);
}
