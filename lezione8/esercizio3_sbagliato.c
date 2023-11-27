//fai una funzione che somma due numeri e mette il risultato in una variabile z

#include <stdio.h>

int somma(int x, int y, int z){
    z=x+y;
}

int main(){
    int x=1;
    int y=5;
    int z=0;
    
    somma(x,y,z);
    printf("%d",z);
}
