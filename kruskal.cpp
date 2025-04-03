#include <iostream>

using namespace std;

void minimo(int m[7][7],int t,int& f,int& c,int& v){
	int min=999;
	for(int i=0;i<t;i++){
		for(int j=0;j<t;j++){
			if (min>m[i][j] && m[i][j]!=0){
				min=m[i][j];
				f=i;
		        c=j;
				v=min;
			}
		}
	}
}

void ponerCero(int m[7][7],int t,int f,int c){
	m[f][c]=0;
	m[c][f]=0;
}

int AristaNueva(int e[6][3],int ti,int tj,int f,int c,int cont){
	int encontradoF=0;
	int encontradoD=0;
	for(int i=0;i<=cont;i++){
		if (e[i][0]==f || e[i][1]==f){
			encontradoF=1;
			break;
		}
		if (e[i][0]==c || e[i][1]==c){
			encontradoD=1;
			break;
		}
	}
	if(encontradoF==1){
		for(int i=0;i<=cont;i++){
			if (e[i][0]==c || e[i][1]==c){
				return 0;
			}
		}
	}
	if(encontradoD==1){
		for(int i=0;i<=cont;i++){
			if (e[i][0]==f || e[i][1]==f){
				return 0;
			}
		}
	}
	return 1;
}

int main(int argc, char *argv[]){
    int t=7;
	int m[7][7]={
		0,7,0, 5, 0,0,0,
		7,0,8, 9, 7,0,0,
		0,8,0, 0,15,0,0,
		5,9,0, 0,15,6,0,
		0,7,15,15, 0,8,9,
		0,0,0, 6, 8,0,11,
		0,0,0, 0, 9,11,0};
	int f,c,v;
	int e[6][3]={-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
	int cont=0;

	while(cont!=6){
		minimo(m,t,f,c,v);
		cout << "minimo: " << f << " " << c << endl;
		ponerCero(m,t,f,c);
		if (cont==0){
			e[cont][0]=f;
			e[cont][1]=c;
			e[cont][2]=v;
			cont++;
		}
		else if (AristaNueva(e,6,3,f,c,cont)){
			e[cont][0]=f;
			e[cont][1]=c;
			e[cont][2]=v;
			cont++;
		}
	}

	for(int i=0;i<6;i++){
		cout << e[i][0] << " " <<
			    e[i][1] << " - " <<
				e[i][2] << endl;
	}

	return 0;
}
