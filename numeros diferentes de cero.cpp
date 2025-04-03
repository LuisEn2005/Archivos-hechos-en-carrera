#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int numero,conteo = 0;
	do{
		cout<<"Digite un numero: ";
		cin>>numero;
		
		if(numero>0){
			conteo++;
		}
	}while(numero != 0);
	
	cout<<"\nEl numero de numeros mayores a cero contados es: "<<conteo<<endl;
	
	getch();
	return 0;
}
