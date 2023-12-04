#include <stdio.h>
#include <stdlib.h>

struct punto{

	int x;
	int y;
};

struct punto punto_medio(struct punto p1, struct punto p2){
	struct punto punto_medio;
	punto_medio.x=(p1.x+p2.x)/2;
	punto_medio.y=(p1.y+p2.y)/2;
	return punto_medio;
}

void stampa_punto(struct punto p){
	printf("(%d,%d)",p.x,p.y);
}

int main(){
	struct punto p1;
	struct punto p2;
	
	p1.x=1;
	p1.y=2;
	
	p2.x=1;
	p2.y=8;
	
	stampa_punto(punto_medio(p1,p2));
}
