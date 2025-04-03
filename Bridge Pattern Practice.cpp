#include <iostream>

using std::cout;
using std::cin;
using std::endl;

class impCalculadora{
public:
    virtual float operar(float a, float b) = 0;
    virtual ~impCalculadora(){}
};

class impSuma : public impCalculadora{
public:
    float operar(float a, float b) override{
        return a + b;
    }
};

class impResta : public impCalculadora{
public:
    float operar(float a, float b) override{
        return a - b;
    }
};

class impProducto : public impCalculadora{
public:
    float operar(float a, float b) override{
        return a * b;
    }
};

class impDivision : public impCalculadora{
public:
    float operar(float a, float b) override{
        while(b == 0){
            cout<<"Divisiones entre 0 no esta permitido." << endl;
            cout<<"Vuelva a ingresar el segundo numero: ";cin >> b;
        }
        return a / b;
    }
};

class Abstraccion{
protected:
    impCalculadora* impCal;
public:
    Abstraccion(impCalculadora* impCal_) : impCal(impCal_){}
    virtual float calcular(float a, float b) = 0;
    virtual ~Abstraccion(){}
};

class absCalculadora : public Abstraccion{
public:
    absCalculadora(impCalculadora* impl) : Abstraccion(impl){}
    float calcular(float a, float b) override{
        return impCal->operar(a,b);
    }
};

int main(){
    int opcion;
    float num1,num2;
    cout<<"Ingrese un numero: ";cin>>num1;
    cout<<"Ingrese un segundo numero: ";cin>>num2;

    cout<<"1. Sumar valores: "<<endl;
    cout<<"2. Restar valores: "<<endl;
    cout<<"3. Producto de valores: "<<endl;
    cout<<"4. Division de valores: "<<endl;
    cout<<"5. salir: "<<endl;
    cout<<"Ingrese una de las opciones (1,2,3,4,5): ";cin>>opcion;

    while(opcion != 5){
        if(opcion == 1){
            impCalculadora* sumar = new impSuma();
            Abstraccion* calc = new absCalculadora(sumar);
            cout<<"Suma: "<<calc->calcular(num1,num2)<<endl;
            delete calc;
            delete sumar;
        }
        else if(opcion == 2){
            impCalculadora* restar = new impResta();
            Abstraccion* calc = new absCalculadora(restar);
            cout<<"Resta: "<<calc->calcular(num1,num2)<<endl;
            delete calc;
            delete restar;
        }
        else if(opcion == 3){
            impCalculadora* producto = new impProducto();
            Abstraccion* calc = new absCalculadora(producto);
            cout<<"Producto: "<<calc->calcular(num1,num2)<<endl;
            delete calc;
            delete producto;

        }
        else if(opcion == 4){
            impCalculadora* division = new impDivision();
            Abstraccion* calc = new absCalculadora(division);
            cout<<"Division: "<<calc->calcular(num1,num2)<<endl;
            delete calc;
            delete division;
        }
        cout<<"Ingrese un numero: ";cin>>num1;
        cout<<"Ingrese un segundo numero: ";cin>>num2;

        cout<<"1. Sumar valores: "<<endl;
        cout<<"2. Restar valores: "<<endl;
        cout<<"3. Producto de valores: "<<endl;
        cout<<"4. Division de valores: "<<endl;
        cout<<"5. salir: "<<endl;
        cout<<"Ingrese una de las opciones (1,2,3,4,5): ";cin>>opcion;
    }
    return 0;
}
