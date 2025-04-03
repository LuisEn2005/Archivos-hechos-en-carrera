#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;
struct pos {
	int i;
	int j;
};

void ceros(int **Ma, int n){
	for(int i=0; i<n;i++)
		for(int j=0; j<n;j++)
			Ma[i][j]=0;
}

void mostrar(int **Ma, int n){
	for(int i=0; i<n;i++){
		for(int j=0; j<n;j++){
			cout<<Ma[i][j]<<" ";
		}
		cout<<endl;
	}
	cout << endl;
}

void caminoBasico(int **Ma, int n){
	for(int i=0;i<(n-1);i++){
		Ma[i][i+1]=1;
		Ma[i+1][i]=1;
	}
}

void aleatorio(int **Ma, int n){
	pos elem;
	vector<pos> v;
	int pos_i,pos_j,aristas,r,cant;
	cant = ((n*n)-n)/2 - (n-1);

	for(int i=0;i<(n-1);i++){
        for(int k=2+i;k<n;k++){
		   elem.i=i;
		   elem.j=k;
		   v.push_back(elem);
		}
	}
	for(size_t i=0;i<v.size();i++){
		cout << "(" << v[i].i<<","<< v[i].j <<")" << endl;
	}
	cout << "Numeros de aristas a ingresar (Max="<<cant << "): ";
	cin >> aristas;

	srand(time(0));

	for(int i=0;i<aristas;i++){
		r=rand()%v.size();
		pos_i=v[r].i;
		pos_j=v[r].j;
		Ma[pos_i][pos_j]=1;
		Ma[pos_j][pos_i]=1;
		v.erase(v.begin()+r);
	}
}
int formaCiclo(int s,int vp[],int t){
	for(int i = 0;i < t; i++){
		if (s == vp[i])
			return 1;
	}
	return 0;
}

int main(int argc, char *argv[]){
    int n;
	cout << "numero de vertices: "; cin >> n;
	int *vp = new int [n];
	int **m = new int *[n];
	for(int i=0; i<n;i++){
		m[i]=new int[n];
	}

	ceros(m,n);
	mostrar(m,n);

	caminoBasico(m,n);
	mostrar(m,n);

	aleatorio(m,n);
	mostrar(m,n);

	const int t = n;
    for(int i = 0;i < t;i++){
        vp[i]= -1;
    }
    int w;
    cout<<"Introduzca el nodo inicial: "; cin>> w;
    cout<<"\n";
	//int w = 3;//nodo inicial
	vp[0] = w;
	int k = 0;
	cout<<"Busqueda en profundidad: \n"<<endl;
	while(1){
		for(int i=0;i<t;i++){
			if (m[w][i]==1){
				if(!formaCiclo(i,vp,t))
				{	k++;
					vp[k]=i;
					cout << w << "-" << vp[k]<< endl;
					w=i;
					break;
				}
			}
			/*Revisar*/
			if (i==(t-1) && k<(t-1))
				w=vp[k-1];
			/*fin revisar*/
		}
		if (vp[t-1]!= -1)
			break;
	}



    delete [] vp;
	for(int i=0;i<n;i++)
		delete [] m[i];
	delete [] m;

	return 0;
}
