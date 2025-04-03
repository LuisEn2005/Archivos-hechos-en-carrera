#include<iostream>
using namespace std;
int main(){
	int n1,n2,n3,n4;
	cout<<"Ingrese 3 numeros: ";cin>>n1>>n2>>n3;
	cout<<"Ingrese un numero: ";cin>>n4;
	if((n4==n1) || (n4==n2) || (n4==n3)){
		cout<<"\nEl cuarto numero es igual a un numero ingresado"<<endl;
	}
	else{
		cout<<"\nEl cuarto numero no es igual a un numero ingresado"<<endl;
	}
	return 0;
}
