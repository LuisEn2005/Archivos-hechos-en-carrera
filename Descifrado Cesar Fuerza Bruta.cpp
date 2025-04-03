#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;
struct letras {
	char l;
	int cant;
};

int i,j,k;

int main() {
	string filename("D:/Projectos C-C++/Programas c++/Descifrado de Cesar fuerza bruta/cifrado.txt");
	FILE* input_file = fopen(filename.c_str(), "r");
	//         a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ' '
	int v[53]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 0};

	int cont=1;
	char c;
	while ((c = fgetc(input_file)) != EOF)
	{
		if (c=='a') v[0]++;
		else if (c=='b') v[1]++;
		else if (c=='c') v[2]++;
		else if (c=='d') v[3]++;
		else if (c=='e') v[4]++;
		else if (c=='f') v[5]++;
		else if (c=='g') v[6]++;
		else if (c=='h') v[7]++;
		else if (c=='i') v[8]++;
		else if (c=='j') v[9]++;
		else if (c=='k') v[10]++;
		else if (c=='l') v[11]++;
		else if (c=='m') v[12]++;
		else if (c=='n') v[13]++;
		else if (c=='o') v[14]++;
		else if (c=='p') v[15]++;
		else if (c=='q') v[16]++;
		else if (c=='r') v[17]++;
		else if (c=='s') v[18]++;
		else if (c=='t') v[19]++;
		else if (c=='u') v[20]++;
		else if (c=='v') v[21]++;
		else if (c=='w') v[22]++;
		else if (c=='x') v[23]++;
		else if (c=='y') v[24]++;
		else if (c=='z') v[25]++;
		else if (c=='A') v[26]++;
		else if (c=='B') v[27]++;
		else if (c=='C') v[28]++;
		else if (c=='D') v[29]++;
		else if (c=='E') v[30]++;
		else if (c=='F') v[31]++;
		else if (c=='G') v[32]++;
		else if (c=='H') v[33]++;
		else if (c=='I') v[34]++;
		else if (c=='J') v[35]++;
		else if (c=='K') v[36]++;
		else if (c=='L') v[37]++;
		else if (c=='M') v[38]++;
		else if (c=='N') v[39]++;
		else if (c=='O') v[40]++;
		else if (c=='P') v[41]++;
		else if (c=='Q') v[42]++;
		else if (c=='R') v[43]++;
		else if (c=='S') v[44]++;
		else if (c=='T') v[45]++;
		else if (c=='U') v[46]++;
		else if (c=='V') v[47]++;
		else if (c=='W') v[48]++;
		else if (c=='X') v[49]++;
		else if (c=='Y') v[50]++;
		else if (c=='Z') v[51]++;
		else if (c==' ') v[52] = 0;
		else
			;//cout << "No definido";

	}

	letras vl[53];
	char ch;
	for(i=0;i<26;i++)
	{
		ch=(i+97);
//		cout << ch << " - " << v[i] << endl;
		vl[i].l=ch;
		vl[i].cant=v[i];
	}
	for(j=0;j<27;j++){
        ch=(j+65);
        vl[j+26].l=ch;
        vl[j+26].cant=v[j+26];
    }
	//ordenar frecuencias
	int temp1;
	char temp2;
	for(k=0;k<53-1;k++)
		for(i=0;i<53-1;i++)
		{
			if (vl[i].cant < vl[i+1].cant)
			{
				temp1=vl[i].cant;
				vl[i].cant=vl[i+1].cant;
				vl[i+1].cant=temp1;

				temp2=vl[i].l;
				vl[i].l=vl[i+1].l;
				vl[i+1].l=temp2;
			}

		}

	for(i=0;i<53;i++){
		cout << vl[i].l << " - " << vl[i].cant << endl;
	}

	int descifrar=1;
	int n;
	if (descifrar==1){
		for(i=0;i<5;i++)
		{   //asumiendo que la letra 'e' es la mas utilizada
			n=vl[i].l - 'e';
			if (n<0)
				n=n+53;
			cout << vl[i].l << " --> k = " << n << endl;
		}
	}

	fclose(input_file);

	return 0;
}
