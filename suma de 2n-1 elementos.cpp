#include<iostream>
#include<conio.h>
using namespace std;
int main(){

	int nElementos,sumaTotal;
	cout<<"Ingrese el numero de elementos a sumar: ";cin>>nElementos;
	for(int i=1;i<=2*nElementos-1;i+=2){
		sumaTotal +=i;
	}
	cout<<"\nLa suma total es: "<<sumaTotal<<endl;
	
	getch();
	return 0;
}
