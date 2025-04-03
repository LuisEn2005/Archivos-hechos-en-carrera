#include<iostream>
using namespace std;
int main(){
	int num;
	cout<<"Ingrese un numero: ";cin>>num;
	if(num==0){
		cout<<"\nEl numero ingresado es cero"<<endl;
	}
	else if(num>0){
		cout<<"\nEl numero ingresado es positivo "<<num<<endl;
	}
	else if(num<0){
		cout<<"\nEl numero ingresado es negativo "<<num<<endl;
	}
	return 0;
}
