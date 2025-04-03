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
void CifradoporFilas(char **Matriz,int f,int c,string texto,int tamanio){
    int x = 0;
    for(int i = 0;i<c;i++){
        for(int j = 0;j<f;j++){
            Matriz[j][i] = texto[x];
            x++;
        }
    }
}

void mostrarpalabrasClave(char **Matriz,int f, int c, string texto, int tamanio){
    cout<<"Palabras cifra"<<endl;
    for(int i = 0;i < f;i++){
        string cifra = "";
        for(int j = 0;j < c;j++){
            cifra += Matriz[i][j];
        }
        cout<<cifra<<endl;
        cifra = "";
    }
}
void descifradoporFilas(char **Matriz, int f, int c,string texto,int tamanio){
    cout<<"Descifrado"<<endl;
    string cifra = "";
    for(int i = 0;i < c;i++){
        for(int j = 0;j < f;j++){
            if(Matriz[j][i] != 'x'){
                cifra += Matriz[j][i];
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
    cout<<"Ingrese cuantas letras debe tener cada linea: ";cin>>filas;
    leerArchivo("D:/Projectos C-C++/Programas c++/Implementacion de criptografia/textoPlano.txt", textoClaro);
    int tamaniotexto = textoClaro.length();
    if(tamaniotexto % filas == 0){
        columnas = tamaniotexto / filas;
    }
    else{
        columnas = (tamaniotexto / filas) + 1;
    }
    modificarfrase(textoClaro,filas,columnas,tamaniotexto);
    crearMatriz(matriz,filas,columnas);
    CifradoporFilas(matriz,filas,columnas,textoClaro,tamaniotexto);
    insertarX(matriz,filas,columnas);
    mostrarMatriz(matriz,filas,columnas);
    mostrarpalabrasClave(matriz,filas,columnas,textoClaro,tamaniotexto);
    descifradoporFilas(matriz,filas,columnas,textoClaro,tamaniotexto);
    borrar(matriz,filas);
    return 0;
}

