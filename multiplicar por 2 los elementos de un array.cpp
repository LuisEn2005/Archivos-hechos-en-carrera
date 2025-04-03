#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	int numeros[] = {1,2,3,4,5};
	int numeros2[5];
	
	for(int i=0;i<5;i++){
		cout<<i<<". Digite los elementos del arreglo: ";
		cin>>numeros[i];
	}
	
	for(int i=0;i<5;i++){
		numeros2[i] = numeros[i]*2;
	}
	
	cout<<"\nMostrando los elementos del arreglo por 2: \n";
	for(int i=0;i<5;i++){
		cout<<numeros2[i]<<" ";
	}
	
	
	getch();
	return 0;
}
