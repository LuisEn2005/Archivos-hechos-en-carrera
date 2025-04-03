#include<iostream>
using namespace std;
int main(){
	int edad;
	cout<<"Introduzca su edad: ";cin>>edad;
	if((edad>=18) && (edad<=25)){
		cout<<"\nUd tiene entre 18 a 25 años de edad"<<endl;
	}
	else{
		cout<<"\nUd no tiene entre 18 a 25 años de edad"<<endl;
	}
}
