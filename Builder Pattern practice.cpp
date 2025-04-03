#include <iostream>

using std::cout;
using std::endl;
using std::cin;
using std::string;

//Producto
class PC{
private:
    string cpu;
    string motherBoard;
    string RAMmemory;
    string disk;
    string GPU;
public:
    void setCpu(const string& cpu){ this->cpu = cpu; }
    void setmotherBoard(const string& motherBoard){ this->motherBoard = motherBoard; }
    void setRam(const string& RAMmemory){ this->RAMmemory = RAMmemory; }
    void setdisk(const string& disk){ this->disk = disk; }
    void setGPU(const string& GPU){ this->GPU = GPU; }
    void mostrarPC()const{
        cout<<"CPU: "<<cpu<<endl;
        cout<<"MOTHERBOARD: "<<motherBoard<<endl;
        cout<<"RAM: "<<RAMmemory<<endl;
        cout<<"DISCO: "<<disk<<endl;
        cout<<"GPU: "<<GPU<<endl;
    }
};

//Builder Abstracto
class construirPC{
public:
    virtual ~construirPC(){}

    virtual void buildCpu() = 0;
    virtual void buildBoard() = 0;
    virtual void buildRam() = 0;
    virtual void buildDisk() = 0;
    virtual void buildGPU() = 0;

    virtual PC* getPC() = 0;
};

//Builder Concreto
class PCGamer : public construirPC{
private:
    PC* computadora;
public:
    PCGamer() { computadora = new PC(); }
    void buildCpu() override{
        computadora->setCpu("Intel Core i5-12600K");
    }
    void buildBoard() override{
        computadora->setmotherBoard("ASUS TUF Gaming Z690-PLUS");
    }
    void buildRam() override{
        computadora->setRam("Corsair Vengeance LPX 16GB");
    }
    void buildDisk() override{
        computadora->setdisk("Samsung 970 EVO Plus 1TB NVMe SSD");
    }
    void buildGPU() override{
        computadora->setGPU("NVIDIA GeForce RTX 3070");
    }
    PC* getPC() override{ return computadora; }
};

//Builder Concreto
class PCparaVideos : public construirPC{
private:
    PC* computadora;
public:
    PCparaVideos() { computadora = new PC(); }
    void buildCpu() override{
        computadora->setCpu("Intel Core i9-12900K");
    }
    void buildBoard() override{
        computadora->setmotherBoard("ASUS ROG Strix Z690-E Gaming WiFi");
    }
    void buildRam() override{
        computadora->setRam("Corsair Vengeance RGB Pro 32GB");
    }
    void buildDisk() override{
        computadora->setdisk("Samsung 970 EVO Plus 2TB NVMe SSD");
    }
    void buildGPU() override{
        computadora->setGPU("NVIDIA GeForce RTX 3080");
    }
    PC* getPC() override{ return computadora; }
};

//Builder Concreto
class PCeconomica : public construirPC{
private:
    PC* computadora;
public:
    PCeconomica() { computadora = new PC(); }
    void buildCpu() override{
        computadora->setCpu("Intel Core i3-12100F");
    }
    void buildBoard() override{
        computadora->setmotherBoard("Gigabyte B660M DS3H");
    }
    void buildRam() override{
        computadora->setRam("Corsair Vengeance LPX 16GB");
    }
    void buildDisk() override{
        computadora->setdisk("Western Digital Blue 1TB HDD");
    }
    void buildGPU() override{
        computadora->setGPU("NVIDIA GeForce GTX 1650");
    }

    PC* getPC() override{ return computadora; }
};

class Director{
private:
    construirPC* construirPc;
public:
    void setbuildPC(construirPC* build){ construirPc = build; }
    PC* getPC(){
        return construirPc->getPC();
    }
    void BuildPC(){
        construirPc->buildCpu();
        construirPc->buildBoard();
        construirPc->buildRam();
        construirPc->buildDisk();
        construirPc->buildGPU();
    }
};

int main(){
    PCGamer PCgamer;
    PCparaVideos PCpro;
    PCeconomica PCeco;

    Director director;

    //director.setbuildPC(&PCgamer);
    director.setbuildPC(&PCpro);
    //director.setbuildPC(&PCeco);

    director.BuildPC();

    PC* pc = director.getPC();
    pc->mostrarPC();

    return 0;
}
