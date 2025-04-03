#include<iostream>
#include<conio.h>
#include<string.h>

using namespace std;

int main(){
	int a,*dir_a;
	
	cout<<"Ingrese un numero: ";cin>>a;
	
	dir_a = &a;
	
	if(*dir_a % 2 != 0){
		cout<<"El numero "<<*dir_a<<" es primo"<<endl;
		cout<<"Posicion "<<dir_a<<endl;
	}
	else{
		cout<<"El numero "<<*dir_a<<" no es primo"<<endl;
		cout<<"Posicion "<<dir_a<<endl;
	}
	return 0;
	getch();
}
