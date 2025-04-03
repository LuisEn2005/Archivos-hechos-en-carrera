#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int num,cont=0;
	do{
		cout<<"ingrese un numero: ";
		cin>>num;
		
		if(num>0){
			cont++;
		}
	}while (num!=0);
	cout<<"el numero de numeros mayores a 0 ingresados es: "<<cont;
	return 0;
}
