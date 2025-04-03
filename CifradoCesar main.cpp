#include <iostream>
using namespace std;

int buscarNumero(char c,string pat){
	for(int i=0;i<pat.length();i++){
		if (c==pat[i]){
			return i;
		}
	}
	return -1;
}

char buscarLetra(int i,string pat){
	return  pat[i];
}

int main(int argc, char *argv[]){
	string patron="0123456789(),:.-_ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz";
	string m;
	string cif="";
	int k;
	int c;
	char txt;
	int pos;
	cout << "Mensaje a cifrar: ";
	getline(cin, m);
	k=3;
	cout << "Factor K (entre 1 y " << patron.length()-1 <<"): ";
	cin >> k;
	//Cifrado
	for(int i=0;i<m.length();i++){
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
