#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	int numeros[100][100],nfilas,ncolumnas;
	char band='F';
	
	cout<<"Digite el numero de filas: ";cin>>nfilas;
	cout<<"Digite el numero de columnas: ";cin>>ncolumnas;
	
	for(int i=0;i<nfilas;i++){
		for(int j=0;j<ncolumnas;j++){
			cout<<"Ingrese un numero["<<i<<"]["<<j<<"]: ";
			cin>>numeros[i][j];
		}
	}
	
	if(nfilas==ncolumnas){
		for(int i=0;i<nfilas;i++){
			for(int j=0;j<nfilas;j++){
				if(numeros[i][j] == numeros[j][i]){
					band='V';
				}
			}
		}
	}
	
	if(band == 'V'){
		cout<<"La matriz es simetrica";
	}
	else{
		cout<<"La matriz no es simetrica";
	}
	
	getch();
	return 0;
}
