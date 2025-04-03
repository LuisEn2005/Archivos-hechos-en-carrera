#include<iostream>
using namespace std;
int main(){
	int num;
	cout<<"ingrese un valor entero: ";cin>>num;
	if(num==0){
		cout<<"\nEl numero ingresado es cero "<<num;
	}
	else if(num%2==0){
		cout<<"\nEl numero ingresado es par "<<num;
	}
	else{
		cout<<"\nEl numero ingresado es impar "<<num;
	}
	return 0;
}
