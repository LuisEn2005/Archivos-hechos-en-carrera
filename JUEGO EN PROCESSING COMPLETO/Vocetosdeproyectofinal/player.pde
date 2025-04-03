class Player extends Animacion
{
  int vidas, estado, timer;
  boolean enPlataforma, enPiso;
  PImage[] irder, irizq, saltoder, saltoizq;
  Player(PImage imagen)
  {
    super(imagen);
    vidas = 3;
    timer = 0;
    dir = derecha;
    estado = 0;
    enPlataforma = false;
    enPiso = false;
    irder = new PImage[2];
    irizq = new PImage[2];
    moverder = new PImage[8];
    moverizq = new PImage[8];
    saltoder = new PImage[1];
    saltoizq = new PImage[1];
    actual = saltoder;
  }
  void cargarEstado()
  {
    if
  }
}
