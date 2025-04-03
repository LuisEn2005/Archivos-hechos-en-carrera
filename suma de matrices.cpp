#include<iostream>
#include<conio.h>

using namespace std;

int main(){
	int numeros[3][3];
	int numeros2[3][3];
	
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<"Ingrese la primera matriz["<<i<<"]["<<j<<"]: ";
			cin>>numeros[i][j];
		}
	}
	
	cout<<"\n1ra matriz\n";
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<numeros[i][j]<<" ";
		}
		cout<<"\n";
	}
	
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<"Ingrese la segunda matriz["<<i<<"]["<<j<<"]: ";
			cin>>numeros2[i][j];
		}
	}
	
	cout<<"\n2da matriz\n";
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<numeros2[i][j]<<" ";
		}
		cout<<"\n";
	}
	
	cout<<"\nSuma de las 2 matrices es: "<<endl;
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<numeros[i][j] + numeros2[i][j]<<" ";
		}
		cout<<"\n";
	}
	
	
	getch();
	return 0;
}
