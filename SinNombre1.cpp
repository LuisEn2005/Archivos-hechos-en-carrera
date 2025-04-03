#include<iostream>
#include<conio.h>
#include<string.h>

using namespace std;

int main(){
	char frase[50];
	
	cout<<"digite una frase: ";
	cin.getline(frase,50,'\n');
	
	if(strlen(frase)>10){
		cout<<"La frase "<<frase<<" supera los 10 caracteres"<<endl;
	}
	else{
		cout<<"La frase "<<frase<<" no supera los 10 caracteres"<<endl;
	}
	
	getch();
	return 0;
}
