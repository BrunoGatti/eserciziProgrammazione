#include <stdio.h>
#include<stdlib.h>

int main(){
	int *a=malloc(sizeof(int)*4);
	for (int i=0;i < 4;i++){
		a[i]=i+1; //assegno ad a il valore i+1 (cioè a[0]=1,a[1]=2,a[2]=3 e a[3]=4)
		printf("%d",a[i]);
	}
}
