#include "GenericStaticArray.h"

template<typename numData>
genstaticArray<numData>::genstaticArray(int tam) : tam(tam){
    this->tam = tam;
    data = new numData[tam];
}

template<typename numData>
genstaticArray<numData>::~genstaticArray(){
    delete []data;
}

template<typename numData>
numData genstaticArray<numData>::getter(int index)const{
    return data[index];
}

template<typename numData>
int genstaticArray<numData>::gettam()const{
    return tam;
}

template<typename numData>
void genstaticArray<numData>::setter(int index,numData val){
    data[index] = val;
}

template<typename numData>
void genstaticArray<numData>::print()const{
    for(int i = 0;i<tam;i++){
        cout<<data[i]<<",";
    }
    cout<<endl;
}

template<typename numData>
genstaticArray<numData>& genstaticArray<numData>::operator=(const genstaticArray& arrayStat){
    if(this != &arrayStat){
        delete[] data;
        tam = arrayStat.tam;
        data = new numData[tam];
        for(int i = 0;i < tam;i++){
            data[i] = arrayStat.data[i];
        }
    }
    return *this;
}

template<typename numData>
bool genstaticArray<numData>::operator==(const genstaticArray& arrayStat)const{
    if(tam != arrayStat.tam){
        return false;
    }
    for(int i = 0;i < tam;i++){
        if(data[i] != arrayStat.data[i]){
            return false;
        }
    }
    return true;
}

template<typename numData>
bool genstaticArray<numData>::operator!=(const genstaticArray& arrayStat)const{
    return !(*this == arrayStat);
}

template<typename numData>
numData& genstaticArray<numData>::operator[](int index) {
    return data[index];
}

template<typename numData>
const numData& genstaticArray<numData>::operator[](int index) const {
    return data[index];
}

template<typename numData>
ostream& operator<<(ostream& out,const genstaticArray<numData>& arr){
    for(int i = 0;i < arr.tam;i++){
        out<<arr.data[i]<<" ";
    }
    return out;
}

template<typename numData>
istream& operator>>(istream& in,genstaticArray<numData>& arr) {
    cout<<"ingrese "<<arr.tam<<" elemento(s): "<<endl;
    for(int i = 0;i < arr.tam;i++){
        cout<<"Elemento ["<<i<<"]: ";
        in>>arr.data[i];
    }
    return in;
}
