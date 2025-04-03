#include<iostream>
using namespace std;
int main(){
	int n1,n2,n3;
	/*
	cout<<"ingrese un numero para determinar el mayor: ";cin>>n1;
	cout<<"ingrese un numero para determinar el mayor: ";cin>>n2;
	cout<<"ingrese un numero para determinar el mayor: ";cin>>n3;
	*/
	cout<<"ingrese 3 numeros para determinar el mayor: ";cin>>n1>>n2>>n3;
	if((n1>=n2) && (n1>=n3)){
		cout<<"\nEl numero mayor es: "<<n1<<endl;
	}
	else if((n2>=n1) && (n2>=n3)){
		cout<<"\nEl numero mayor es: "<<n2<<endl;
	}
	else{
		cout<<"\nEl numero mayor es: "<<n3<<endl;
	}
	return 0;
}
