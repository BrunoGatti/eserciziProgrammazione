#include <stdio.h>
float aumenta(float * puntatore_a_num1, int num2){
	*puntatore_a_num1 += num2;
}
int main(){
	float pi=3.14;
	aumenta(&pi, 1);
	printf("%f\n",pi);
}
