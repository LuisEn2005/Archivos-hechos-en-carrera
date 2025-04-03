#include <iostream>
#include <random>

using std::cout;
using std::cin;
using std::endl;

const int filas = 8;
const int columnas = 8;

void crearTablero(int tablero[filas][columnas]){
    for(int i = 0;i < filas;i++){
        for(int j = 0;j < columnas;j++){
            tablero[i][j] = 0;
        }
    }
}
void mostrarTablero(int tablero[filas][columnas]){
    for(int i = 0;i < filas;i++){
        for(int j = 0;j < columnas;j++){
            cout<<tablero[i][j]<<" ";
        }
        cout<<endl;
    }
}
void posAleatorias(int tablero[filas][columnas],std::mt19937& gen){
    int horizontales[4] = {-2,2,1,-1};
    int verticales1[2] = {1,-1};
    int verticales2[2] = {-2,2};
    int contador = 0,i = 4,j = 4;

    while(contador != 64){
        std::uniform_int_distribution<int> dist_hor(0,sizeof(horizontales) / sizeof(horizontales[0]) - 1);
        int randhor = horizontales[dist_hor(gen)];
        int randver;
        if(randhor == -2 || randhor == 2){
            std::uniform_int_distribution<int> dist_ver1(0,sizeof(verticales1) / sizeof(verticales2[0])-1);
            randver = verticales1[dist_ver1(gen)];
        }
        else{
            std::uniform_int_distribution<int> dist_ver2(0,sizeof(verticales2) / sizeof(verticales2[0])-1);
            randver = verticales2[dist_ver2(gen)];
        }
        int newi = i+randver;
        int newj = j+randhor;
        if(newi >= 0 && newi < filas && newj >= 0 && newj < columnas){
            i = newi;
            j = newj;
            tablero[i][j] += 1;
            contador++;
        }
    }
}

int main(){
    int tablero[filas][columnas];

    std::random_device rd;
    std::mt19937 gen(rd());

    crearTablero(tablero);
    posAleatorias(tablero,gen);
    mostrarTablero(tablero);
    posAleatorias(tablero,gen);
    mostrarTablero(tablero);
    return 0;
}
