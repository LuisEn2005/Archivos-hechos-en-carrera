#include <iostream>

using namespace std;

void crearMatriz(int **&Matriz,int filas,int columnas){
    Matriz = new int*[filas];
    for(int i = 0;i < filas;i++){
        Matriz[i] = new int[columnas];
    }
}

void insertarMatriz(int **Matriz,int filas,int columnas){
    int elemento;
    for(int i = 0;i<filas;i++){
        for(int j = 0;j<columnas;j++){
            cout<<"Ingresando elementos de la matriz ("<<i<<")("<<j<<"): "; cin>>elemento;
            Matriz[i][j] = elemento;
        }
    }
}

void mostrarMatriz(int **Matriz,int filas,int columnas){
    for(int i = 0;i<filas;i++){
        for(int j = 0;j<columnas;j++){
            cout<<Matriz[i][j]<<" ";
        }
        cout<<"\n";
    }
}
void verifCuadradoMagico(int **Matriz, int filas, int columnas){
    int suma = 0;
    int suma_total;
    int casos = 0;
    int error = 0;
    while(casos != 4){
        switch(casos){
            case 0:
                cout<<"Calculando las filas: "<<endl;
                for(int i = 0;i<filas;i++){
                    suma = 0;
                    for(int j = 0; j<columnas; j++){
                        suma += Matriz[i][j];
                        cout<<suma<<endl;
                    }
                    if(suma != suma){
                        cout<<"La suma "<<suma<<" no es igual al total "<<suma_total<<endl;
                        casos++;
                        error++;
                        break;
                    }
                }
                suma_total = suma;
                cout<<"sumatotal = "<<suma_total<<"\n"<<endl;
                casos++;
                break;
            case 1:
                cout<<"Calculando las columnas: "<<endl;
                for(int i = 0;i<filas;i++){
                    suma = 0;
                    for(int j = 0; j<columnas; j++){
                        suma += Matriz[j][i];
                        cout<<suma<<endl;
                    }
                    if(suma != suma_total){
                        cout<<"La suma "<<suma<<" no es igual al total "<<suma_total<<endl;
                        casos++;
                        error++;
                        break;
                    }
                }
                casos++;
                break;
            case 2:
                suma = 0;
                cout<<"Calculando la diagonal principal: "<<endl;
                for(int i = 0;i<filas;i++){
                    for(int j = 0; j<columnas; j++){
                        if(i == j){
                            suma += Matriz[i][j];
                            cout<<suma<<endl;
                        }
                    }
                }
                if(suma != suma_total){
                    cout<<"La suma "<<suma<<" no es igual al total "<<suma_total<<endl;
                    casos++;
                    error++;
                    break;
                }
                casos++;
                break;
            case 3:
                suma = 0;
                cout<<"Calculando la diagonal secundaria: "<<endl;
                for(int i = 0;i<filas;i++){
                    for(int j = 0; j<columnas; j++){
                        if(i + j == filas - 1){
                            suma += Matriz[i][j];
                            cout<<suma<<endl;
                        }
                    }
                }
                if(suma != suma_total){
                    cout<<"La suma "<<suma<<" no es igual al total "<<suma_total<<endl;
                    casos++;
                    error++;
                    break;
                }
                casos++;
                break;
        }
    }
    if(error > 0){
        cout<<"El cuadrado no es magico";
    }
    else{
        cout<<"El cuadrado es magico";
    }
}
void Borrar(int **Matriz,int filas,int columnas){
    for(int i = 0;i<filas;i++){
        delete[] Matriz[i];
    }
    delete[] Matriz;
}

int main(){
    int **Matriz, filas, columnas;

    cout<<"Ingrese la cantidad de filas: ";
    cin>>filas;
    cout<<"Ingrese la cantidad de columnas: ";
    cin>>columnas;

    crearMatriz(Matriz,filas,columnas);
    insertarMatriz(Matriz,filas,columnas);
    mostrarMatriz(Matriz,filas,columnas);
    verifCuadradoMagico(Matriz,filas,columnas);
    Borrar(Matriz,filas,columnas);
}
