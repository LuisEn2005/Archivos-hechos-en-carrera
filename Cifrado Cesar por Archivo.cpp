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

int buscarNumero(char c,string pat)
{
	for(int i=0;i<pat.length();i++)
	{
		if (c==pat[i])
			return i;
	}
	return -1;
}

char buscarLetra(int i,string pat)
{
	return  pat[i];
}

int main(int argc, char *argv[])
{
	string patron="0123456789\n(),:.ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz";
	string m;
	string cif="";
	int k;
	int c;
	char txt;
	int pos;
	//m="la accion del ser humano en los ecosistemas ha provocado";
	//cout << "Mensaje a cifrar: ";
	leerArchivo("D:/Projectos C-C++/Programas c++/Cifrado Cesar/TextoPlano.txt", m);
	k=3;
	cout << "Factor K (entre 1 y " << patron.length()-1 <<"): ";
	cin >> k;
	//Cifrado
	for(int i=0;i<m.length();i++)
	{
		pos=buscarNumero(m[i],patron);
		c = (pos+k) % patron.length();
		txt=buscarLetra(c,patron);
		cif.append(1, txt);
	}
	cout << endl;
	cout << cif << endl;
	cout << endl;
	//Descifrado
	for(int i=0;i<cif.length();i++)
	{
		pos=buscarNumero(cif[i],patron);
		c = ((pos-k)+ (patron.length()) ) % patron.length();
		txt=buscarLetra(c,patron);
		cout << txt;
	}
	cout << endl;

	return 0;
}
