#include <iostream>
#include <cmath>

using std::cout;
using std::endl;
using std::string;

class Vehiculo{
protected:
    int Placa;
    int Pasajeros;
public:
    Vehiculo(int _Placa,int _Pasajeros) : Placa(_Placa),Pasajeros(_Pasajeros){}
    void setPlaca(int _Placa){
        Placa = _Placa;
    }
    void setPasajeros(int _Pasajeros){
        Pasajeros = _Pasajeros;
    }
    int getPlaca(){
        return Placa;
    }
    int getPasajeros(){
        return Pasajeros;
    }
};

class Car : public Vehiculo{
private:
    int Velocidad;
    string Marca;
public:
    Car(int _Placa,int _Pasajeros,int _Velocidad,string _Marca) : Vehiculo(_Placa,_Pasajeros), Velocidad(_Velocidad),Marca(_Marca){}
    Car() : Vehiculo(0,0),Velocidad(0), Marca(""){}
    void setVelocidad(int _Velocidad){
        Velocidad = _Velocidad;
    }
    void setMarca(string _Marca){
        Marca = _Marca;
    }
    int getVelocidad(){
        return Velocidad;
    }
    string getMarca(){
        return Marca;
    }
};
class Punto{
    int x,y;
public:
    Punto(int _x, int _y):x(_x),y(_y){}
    void setx(int _x){x=_x;}
    void sety(int _y){y=_y;}
    int getx()const{return x;}
    int gety()const{return y;}
    void print()const{
        cout<<"("<<x<<","<<y<<")";
    }
};
class vectorG{
    Punto ini,fin;
    int modulo;
public:
    vectorG(Punto _ini,Punto _fin):ini(_ini),fin(_fin){
        modulo = showModulo();
    }
    void setPuntoI(Punto _ini){ini = _ini;}
    void setPuntoF(Punto _fin){fin = _fin;}
    int showModulo()const{
        int dx = fin.getx() - ini.getx();
        int dy = fin.gety() - ini.gety();
        return sqrt(dx*dx + dy*dy);
    }
};
int main(){
    Car carro;
    carro.setPlaca(11001010);
    carro.setPasajeros(5);
    carro.setMarca("Volkswagen");
    carro.setVelocidad(80);
    Car* tractor = new Car();
    Car* carritowe = new Car();

    tractor->setPlaca(10010110);
    tractor->setPasajeros(2);
    tractor->setMarca("Scania");
    tractor->setVelocidad(180);

    carritowe->setPlaca(2024);
    carritowe->setPasajeros(3);
    carritowe->setMarca("tico we");
    carritowe->setVelocidad(30);

    Punto punto1(8,5);
    Punto punto2(4,2);
    vectorG vector1(punto1,punto2);

    cout<<"Placa del vehiculo: "<<carro.getPlaca()<<'\n';
    cout<<"Pasajeros del vehiculo: "<<carro.getPasajeros()<<'\n';
    cout<<"Marca del vehiculo: "<<carro.getMarca()<<'\n';
    cout<<"Velocidad del vehiculo: "<<carro.getVelocidad()<<"Km/h"<<'\n';

    cout<<"Placa del vehiculo: "<<tractor->getPlaca()<<'\n';
    cout<<"Pasajeros del vehiculo: "<<tractor->getPasajeros()<<'\n';
    cout<<"Marca del vehiculo: "<<tractor->getMarca()<<'\n';
    cout<<"Velocidad del vehiculo: "<<tractor->getVelocidad()<<"Km/h"<<'\n';

    cout<<"Placa del vehiculo: "<<carritowe->getPlaca()<<'\n';
    cout<<"Pasajeros del vehiculo: "<<carritowe->getPasajeros()<<'\n';
    cout<<"Marca del vehiculo: "<<carritowe->getMarca()<<'\n';
    cout<<"Velocidad del vehiculo: "<<carritowe->getVelocidad()<<"Km/h"<<'\n';

    cout<<"Modulo: "<<vector1.showModulo();

    delete tractor;
    delete carritowe;
    return 0;
}
