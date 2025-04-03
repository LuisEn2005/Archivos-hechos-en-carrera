#include <iostream>

using namespace std;

class Persona{
private:
    string Nombre;
    int Dinero;
public:
    Persona(string _name, int _money) : Nombre(_name), Dinero(_money){}
    void retirar(int plata){
        Dinero -= plata;
    }
    void aumentar(int plata){
        Dinero += plata;
    }
    void MostrarDinero(){
        cout<<"Cantidad de dinero actual: S/"<<Dinero<<endl;
    }
    void mostrarPersona(){
        cout<<"Nombre: "<<Nombre<<endl;
        cout<<"Dinero: S/"<<Dinero<<endl;
    }
};

class Joven : public Persona{
private:
    int estado;
public:
    Joven(string _name, int _money, int _estado) : Persona(_name,_money),estado(_estado){}
    void reduccion_aumento(){
        if(estado == 1){
            cout<<"Se le reducira 200 soles"<<endl;
            retirar(200);
        }
        if(estado == 2){
            cout<<"Se le aumentara 800 soles"<<endl;
            aumentar(800);
        }
        if(estado == 3){
            cout<<"Se le dara un descuento de 100 soles en estudio de parte de su sueldo"<<endl;
            aumentar(700);
        }
        MostrarDinero();
    }
    void mostrardatosJoven(){
        mostrarPersona();
        cout<<"Estado: ";
        if(estado == 1){
            cout<<"El usuario estudia."<<endl;
        }
        if(estado == 2){
            cout<<"El usuario trabaja."<<endl;
        }
        if(estado == 3){
            cout<<"El usuario estudia y trabaja."<<endl;
        }
        reduccion_aumento();
    }
};

int main(){
    string nombre;
    int estado;
    int ingresos;
    cout<<"Ingrese su nombre: ";
    getline(cin,nombre);
    cout<<"Escriba \"1\" si estudia, \"2\" si trabaja, \"3\" si estudia y trabaja: ";
    cin>>estado;
    cout<<"Ingrese la cantidad de sus ingresos (en soles): ";
    cin>>ingresos;
    Joven jovencito1(nombre,ingresos,estado);

    jovencito1.mostrardatosJoven();
    return 0;
}
