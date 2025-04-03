#include <iostream>

using namespace std;

int suma(int n1, int n2){
    int adicion = n1 + n2;
    return adicion;
}
int resta(int n1, int n2){
    int sustraccion = n1 - n2;
    return sustraccion;
}
int multiplicacion(int n1, int n2){
    int producto = n1 * n2;
    return producto
}
float division(int n1, int n2){
    int fraccion = n1 / n2;
    return fraccion;
}

int main(){
    int n1, n2;
    cout<<"Ingrese un numero: ";
    cin>>n1;
    cout<<"Ingrese otro numero: ";
    cin>>n2;

    cout<<"La suma es: "<<suma(n1,n2)<<endl;
    cout<<"La resta es: "<<resta(n1,n2)<<endl;
    cout<<"La multiplicacion es: "<<multiplicacion(n1,n2)<<endl;
    cout<<"La division es: "<<division(n1,n2)<<endl;

    return 0;
}
