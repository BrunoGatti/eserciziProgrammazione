#include <stdio.h>
int main(){
	int a[3]={1,2,3};
	int *b=a;
	for (int i=0;i<3;i++){
		printf("%d",*(b+i));
	}
}
