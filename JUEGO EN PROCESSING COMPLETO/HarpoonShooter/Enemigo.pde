class Enemigo extends Naves{
    int vida=1;
    Enemigo(int xpos,int ypos){
        x = xpos;
        y = ypos;
        sprite = new String[5];
        sprite[0] = "1111111";
        sprite[1] = "1011101";
        sprite[2] = "1111111";
        sprite[3] = "0101010";
        sprite[4] = "1101011";
    }
    void ActualizarNav() {
        if (frameCount % 30 == 0) {
            x += direccion * tamcuadricula;
        }
    }
    boolean Vivo(){
        for (int i = 0; i < balas.size(); i++) {
            Balas bala = (Balas) balas.get(i);
            if (bala.x > x && bala.x < x + 7 * tampixel + 5 && bala.y > y && bala.y < y + 5 * tampixel) {
                balas.remove(i);
                vida--;                
                if (vida == 0) {
                    puntos += 50;
                    return false;
                }               
            }
        }
        return true;
    }
    boolean Afuera() {
        return x + (direccion*tamcuadricula) < 0 || x + (direccion*tamcuadricula) > width - tamcuadricula;
    }
}
