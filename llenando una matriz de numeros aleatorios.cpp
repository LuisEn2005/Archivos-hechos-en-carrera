#include<iostream>
#include<conio.h>
#include<stdlib.h>
#include<time.h>

using namespace std;

int main(){
	int numeros[100][100],dato,nfilas,ncol;
	int numeros2[100][100];
	
	
	cout<<"Digite el numero de filas: ";
	cin>>nfilas;
	cout<<"Digite el numero de columnas: ";
	cin>>ncol;
	
	srand(time(NULL)); //genera numeros aleatorios
	
	
	//rellena la matriz de numeros aleatorios 
	for(int i=0;i<nfilas;i++){
		for(int j=0;j<ncol;j++){
			dato = 1+rand()%(100); //genera numeros aleatorios del 1 al 100
			numeros2[i][j] = dato;
		}
	}
	//copiar el contenido a otra matriz
	for(int i=0;i<nfilas;i++){
		for(int j=0;j<ncol;j++){
			cout<<numeros2[i][j]<<" ";
		}
		cout<<"\n";
	}
	
	
	
	
	getch();
	return 0;
}
