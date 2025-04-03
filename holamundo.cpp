#include<iostream>
using namespace std;
int main(){
	int n1,n2, suma=0, resta=0, multiplicacion=0,division=0;
	int entero = 40;
	float flotante = 24.23;
	double bigflotante = 42.21;
	char when = 'a';
	cout<<"ingrese un número: ";cin>>n1;
	cout<<"ingrese un segundo número: ";cin>>n2;
	suma = n1+n2;
	resta = n1-n2;
	multiplicacion = n1*n2;
	division = n1/n2;
    cout<<"la suma entre los dos numeros es: "<<suma<<endl;
    cout<<"la resta entre los dos numeros es: "<<resta<<endl;
    cout<<"la multiplicacion entre los dos numeros es: "<<multiplicacion<<endl;
    cout<<"la division entre los dos numeros es: "<<division<<endl;
    cout<<entero<<flotante<<bigflotante<<when;
    return 0;
}

