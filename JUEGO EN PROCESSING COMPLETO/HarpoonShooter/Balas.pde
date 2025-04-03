class Balas {
    float x,y;
    Balas(float xpos, float ypos) {
        x = xpos + tamcuadricula/2 - 4;
        y = ypos;
    }
    void draw(){
        fill(104,74,26);
        rect(x,y,10,50);
        y -= 10;
    }
}
