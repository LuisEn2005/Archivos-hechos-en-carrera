#include<iostream>
using namespace std;
int main(){
	char letra;
	cout<<"Digite un caracter: ";cin>>letra;
	switch(letra){
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':cout<<"\nEs una vocal minuscula";break;
		default :cout<<"\nNo es una vocal minuscula";break;
	}
	return 0;
}
