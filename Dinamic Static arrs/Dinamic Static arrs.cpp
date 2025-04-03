#include <iostream>
#include "GenericDynamicArray.h"
#include "GenericStaticArray.h"

using std::cout;
using std::cin;
using std::endl;
using std::ostream;
using std::istream;

int main() {
    genstaticArray<int> arr(5);

    cout << "STATIC ARRAY: " << endl;
    cout << '\n';
    cout << "Tamanio: " << arr.gettam() << endl;
    arr.setter(0, 1);
    arr.setter(1, 2);
    arr.setter(2, -3);
    arr.setter(3, 4);
    arr.setter(4, -5);
    arr.print();

    genstaticArray<float> arr2(5);
    cout << "Tamanio: " << arr2.gettam() << endl;
    arr2.setter(0, 0.5f);
    arr2.setter(1, 3.5f);
    arr2.setter(2, 2.2f);
    arr2.setter(3, 0.9f);
    arr2.setter(4, -1.4f);
    arr2.print();

    genstaticArray<int> arr1(5);
    cin >> arr1;
    cout << "Array arr1: " << arr1 << endl;

    genstaticArray<int> arr4 = arr;
    cout << "Array arr4: " << arr4 << endl;

    if (arr == arr4) {
        cout << "Los arr y arr4 son iguales" << endl;
    }
    else {
        cout << "Los arr y arr4 no son iguales" << endl;
    }

    if (arr != arr1) {
        cout << "Los arr y arr1 no son iguales" << endl;
    }
    else {
        cout << "Los arr y arr1 son iguales" << endl;
    }
    cout << "Uso del operador [] sobrecargado (array Estatico): " << endl;
    for (int i = 0; i < arr2.gettam(); i++) {
        cout << arr2[i] << endl;
    }

    cout << '\n';
    cout << "DYNAMIC ARRAYS: " << endl;
    int arr3[] = { 1,2,3 };
    DynamicArray<int> b(arr3, 3);
    b.Psh_Back(15);
    b.print();
    b.Inserter(1, 3);
    b.Psh_Back(80);
    b.Psh_Back(13);
    b.print();
    b.Inserter(2, 10);
    b.print();
    b.Inserter(5, 10);
    b.print();
    b.Remover(4);
    b.print();
    b.Remover(4);
    b.print();

    DynamicArray<int> c(arr3, 3);
    if (b == c) {
        cout << "Los arrays B y C son iguales" << endl;
    }
    else {
        cout << "Los arrays B y C no son iguales" << endl;
    }

    cout << "Array b: " << b << endl;
    DynamicArray<int> d;
    cin >> d;
    cout << "Array d: " << d << endl;

    if (b == d) {
        cout << "Los arrays B y D son iguales" << endl;
    }
    else {
        cout << "Los arrays B y D no son iguales" << endl;
    }
    cout << "Uso del operador [] sobrecargado (array Dinamico): " << endl;

    for (int i = 0; i < b.getTam(); i++) {
        cout << b[i] << endl;
    }
    return 0;
}
