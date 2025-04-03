#include <iostream>

using namespace std;

int formaCiclo(int s, int vp[],int t){
    for(int i = 0;i < t;i++){
        if(s == vp[i]){
            return 1;
        }
    }
    return 0;
}

int main(){

}
