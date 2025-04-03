#include<iostream>
#include<conio.h>
using namespace std;
int main(){
	int x,y,elevacion=1;
	
	cout<<"Digite el valor de X: ";
	cin>>x;
	cout<<"Digite el valor de y: ";
	cin>>y;
	for (int i=1;i<=y;i++){
		elevacion = elevacion * x;
	}
	cout<<"\nEl resultado de la elevacion es: "<<elevacion<<endl;
	getch();
	return 0;
}

