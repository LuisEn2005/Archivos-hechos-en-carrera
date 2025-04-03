#include <iostream>
#include <fstream>

using namespace std;

void leerArchivo(string nombreArchivo, string &contenido) {
    ifstream archivo(nombreArchivo);

    if (archivo.is_open()) {
        contenido.assign((istreambuf_iterator<char>(archivo)),
                         (istreambuf_iterator<char>()));
        archivo.close();
    } else {
        cerr << "Error al abrir el archivo: " << nombreArchivo << endl;
    }
}
void crearMatriz(char **&Matriz,int f,int c){
    Matriz = new char*[f];
    for(int i = 0;i<f;i++){
        Matriz[i]= new char[c];
    }
}
void modificarfrase(string texto,int f,int c,int tamanio){
    for(int i = tamanio;i<f*c;i++){
        texto[i] = '\0';
    }
}
void insertarX(char **Matriz,int f,int c){
    for(int i = 0;i<f;i++){
        for(int j = 0;j<c;j++){
            if(Matriz[i][j] == '\0'){
                Matriz[i][j] = 'x';
            }
        }
    }
}
void CifradoporColumnas(char **Matriz,int f,int c,string texto,int tamanio){
    int x = 0;
    for(int i = 0;i<f;i++){
        for(int j = 0;j<c;j++){
            Matriz[i][j] = texto[x];
            x++;
        }
    }
}

void mostrarpalabrasClave(char **Matriz,int f, int c, string texto, int tamanio){
    cout<<"Palabras cifra"<<endl;
    for(int i = 0;i < c;i++){
        string cifra = "";
        for(int j = 0;j < f;j++){
            cifra += Matriz[j][i];
        }
        cout<<cifra<<endl;
        cifra = "";
    }
}
void descifradoporColumnas(char **Matriz, int f, int c,string texto,int tamanio){
    cout<<"Descifrado"<<endl;
    string cifra = "";
    for(int i = 0;i < f;i++){
        for(int j = 0;j < c;j++){
            if(Matriz[i][j] != 'x'){
                cifra += Matriz[i][j];
            }
        }
    }
    cout<<cifra<<endl;
}
void mostrarMatriz(char **Matriz,int f,int c){
    for(int i = 0;i<f;i++){
        for(int j = 0;j<c;j++){
            cout<<Matriz[i][j]<<" ";
        }
        cout<<"\n";
    }
}
void borrar(char **&Matriz,int f){
    for(int i = 0;i<f;i++){
        delete [] Matriz[i];
    }
    delete [] Matriz;
}
int main(){
    string textoClaro;
    char **matriz;
    int filas, columnas;
    cout<<"Ingrese cuantas letras debe tener cada linea: ";cin>>columnas;
    leerArchivo("D:/Projectos C-C++/Programas c++/Implementacion de criptografia/textoPlano.txt", textoClaro);
    int tamaniotexto = textoClaro.length();
    if(tamaniotexto % columnas == 0){
        filas = tamaniotexto / columnas;
    }
    else{
        filas = (tamaniotexto / columnas) + 1;
    }
    modificarfrase(textoClaro,filas,columnas,tamaniotexto);
    crearMatriz(matriz,filas,columnas);
    CifradoporColumnas(matriz,filas,columnas,textoClaro,tamaniotexto);
    insertarX(matriz,filas,columnas);
    mostrarMatriz(matriz,filas,columnas);
    mostrarpalabrasClave(matriz,filas,columnas,textoClaro,tamaniotexto);
    descifradoporColumnas(matriz,filas,columnas,textoClaro,tamaniotexto);
    borrar(matriz,filas);
    return 0;
}
