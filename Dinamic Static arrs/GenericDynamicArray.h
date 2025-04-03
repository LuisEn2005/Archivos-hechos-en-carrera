#include <iostream>

using std::cout;
using std::cin;
using std::endl;
using std::ostream;
using std::istream;

template<typename Dynanum>
class DynamicArray{
    int tam;
    Dynanum *dato;
public:
    DynamicArray();
    DynamicArray(Dynanum arr[],int tam);
    DynamicArray(const DynamicArray &o);
    DynamicArray& operator=(const DynamicArray &arrayDin);
    ~DynamicArray();

    int getTam()const;
    void Psh_Back(Dynanum val);
    void Inserter(int pos,Dynanum val);
    void Remover(int pos);
    void print()const;

    bool operator==(const DynamicArray &arrayDin) const;
    bool operator!=(const DynamicArray &arrayDin) const;

    Dynanum& operator[](int index);
    const Dynanum& operator[](int index) const;

    template<typename T>
    friend ostream& operator<<(ostream &out, const DynamicArray<T> &arr);

    template<typename T>
    friend istream& operator>>(istream &in, DynamicArray<T> &arr);
};
template<typename Dynanum>
DynamicArray<Dynanum>::DynamicArray() {
    this->tam = 0;
    dato = new Dynanum[tam];
}

template<typename Dynanum>
DynamicArray<Dynanum>::DynamicArray(Dynanum arr[], int tam) {
    this->tam = tam;
    dato = new Dynanum[tam];
    for (int i = 0; i < tam; i++) {
        dato[i] = arr[i];
    }
}

template<typename Dynanum>
DynamicArray<Dynanum>::DynamicArray(const DynamicArray& o) {
    this->tam = o.tam;
    dato = new Dynanum[tam];
    for (int i = 0; i < tam; i++) {
        dato[i] = o.dato[i];
    }
}

template<typename Dynanum>
DynamicArray<Dynanum>& DynamicArray<Dynanum>::operator=(const DynamicArray& arrayDin) {
    if (this != &arrayDin) {
        delete[] dato;
        tam = arrayDin.tam;
        dato = new Dynanum[tam];
        for (int i = 0; i < tam; i++) {
            dato[i] = arrayDin.dato[i];
        }
    }
    return *this;
}

template<typename Dynanum>
DynamicArray<Dynanum>::~DynamicArray() {
    delete[]dato;
}

template<typename Dynanum>
bool DynamicArray<Dynanum>::operator==(const DynamicArray& arrayDin)const {
    if (tam != arrayDin.tam) {
        return false;
    }
    for (int i = 0; i < tam; i++) {
        if (dato[i] != arrayDin.dato[i]) {
            return false;
        }
    }
    return true;
}

template<typename Dynanum>
bool DynamicArray<Dynanum>::operator!=(const DynamicArray& arrayDin)const {
    return !(*this == arrayDin);
}

template<typename Dynanum>
Dynanum& DynamicArray<Dynanum>::operator[](int index) {
    return dato[index];
}

template<typename Dynanum>
const Dynanum& DynamicArray<Dynanum>::operator[](int index)const {
    return dato[index];
}

template<typename Dynanum>
int DynamicArray<Dynanum>::getTam()const {
    return tam;
}

template<typename Dynanum>
void DynamicArray<Dynanum>::Psh_Back(Dynanum val) {
    int tamanio = tam + 1;
    Dynanum* tmp = new Dynanum[tamanio];
    for (int i = 0; i < tam; i++) {
        tmp[i] = dato[i];
    }
    tmp[tamanio] = val;
    delete[] dato;
    dato = tmp;
    ++tam;
}
template<typename Dynanum>
void DynamicArray<Dynanum>::Inserter(int pos, Dynanum val) {
    Dynanum* tmp = new Dynanum[tam + 1];
    for (int i = 0; i < pos; i++) {
        tmp[i] = dato[i];
    }
    tmp[pos] = val;
    for (int i = pos; i < tam; i++) {
        tmp[i + 1] = dato[i];
    }
    delete[] dato;
    dato = tmp;
    ++tam;
}
template<typename Dynanum>
void DynamicArray<Dynanum>::Remover(int pos) {
    int tamanio = tam - 1;
    Dynanum* tmp = new Dynanum[tamanio];
    for (int i = 0; i < pos; i++) {
        tmp[i] = dato[i];
    }
    for (int i = pos + 1; i < tam; i++) {
        tmp[i - 1] = dato[i];
    }
    delete[]dato;
    dato = tmp;
    --tam;
}
template<typename Dynanum>
void DynamicArray<Dynanum>::print()const {
    for (int i = 0; i < tam; i++) {
        cout << dato[i] << " ";
    }
    cout << endl;
}

template<typename Dynanum>
ostream& operator<<(ostream& out, const DynamicArray<Dynanum>& arr) {
    for (int i = 0; i < arr.tam; i++) {
        out << arr.dato[i] << " ";
    }
    return out;
}

template<typename Dynanum>
istream& operator>>(istream& in, DynamicArray<Dynanum>& arr) {
    cout << "Ingresar tamanio para array: ";
    in >> arr.tam;

    delete[] arr.dato;
    arr.dato = new Dynanum[arr.tam];

    for (int i = 0; i < arr.tam; i++) {
        cout << "Ingresando elemento [" << i << "]: ";
        in >> arr.dato[i];
    }
    return in;
}