#include<iostream>
using namespace std;
int main(){
	char letra;
	cout<<"\nIngrese un caracter: ";cin>>letra;
	switch(letra){
		case 'a':
		case 'e':
		case 'i':
		case 'o':
		case 'u':cout<<"\nEs una vocal minuscula"<<endl;break;
		case 'A':
		case 'E':
		case 'I':
		case 'O':
		case 'U':cout<<"\nEs una vocal mayuscula"<<endl;break;
		default :cout<<"\nNo es una vocal mayuscula ni minuscula"<<endl;break;
	}
	return 0;
}
