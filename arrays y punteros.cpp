#include<iostream>
#include<conio.h>
#include<string.h>

using namespace std;

int main(){
	int numeros[] = {1,2,3,4,5};
	int *dir_numeros;
	
	dir_numeros = numeros;
	
	for(int i=0;i<5;i++){
		cout<<"Elemento del vector ["<<i<<"]: "<<*dir_numeros++<<endl;
		//cout<<"Posiciones de memoria: "<<numeros[i]<<" es: "<<dir_numeros++<<endl;
	}
	//solo uno de los dos puede funcionar a la vez
	
	
	getch();
	return 0;
}
