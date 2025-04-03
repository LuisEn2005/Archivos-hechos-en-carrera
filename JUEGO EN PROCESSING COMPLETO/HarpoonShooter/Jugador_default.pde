class Personaje extends Animacion{
  int vidas,estado;
  boolean enSuelo,enPiso;
  PImage[] irDer,irIzq,saltoDer,saltoIzq;
  Personaje(PImage imagen){
    super(imagen);
    dir=derecha;
    estado=0;
    enSuelo=false;
    enPiso=false;
    irDer=new PImage[4];
    irIzq=new PImage[4];
    moverDer=new PImage[10];
    moverIzq=new PImage[10];
    estado();
  }
  void estado(){
    if(estado == 0){
      irIzq[0]=personaje[7];
      irIzq[1]=personaje[8];
      irIzq[2]=personaje[9];
      irIzq[3]=personaje[8];
      irDer[0]=personaje[0];
      irDer[1]=personaje[1];
      irDer[2]=personaje[2];
      irDer[3]=personaje[1];
      moverDer[0]=personaje[10];
      moverDer[1]=personaje[11];
      moverDer[2]=personaje[12];
      moverDer[3]=personaje[13];
      moverDer[4]=personaje[14];
      moverDer[5]=personaje[15];
      moverDer[6]=personaje[16];
      moverDer[7]=personaje[17];
      moverDer[8]=personaje[18];
      moverDer[9]=personaje[19];
      moverIzq[0]=personaje[29];
      moverIzq[1]=personaje[28];
      moverIzq[2]=personaje[27];
      moverIzq[3]=personaje[26];
      moverIzq[4]=personaje[25];
      moverIzq[5]=personaje[24];
      moverIzq[6]=personaje[23];
      moverIzq[7]=personaje[22];
      moverIzq[8]=personaje[21];
      moverIzq[9]=personaje[20];
    }
  }
  @Override
  void actualizar(){
    enSuelo=estaEnSuelo(this,suelo);
    enPiso=cambio.x==0 && cambio.y==0;
    super.actualizar();
  }
  @Override
  void seleccionarDireccion(){
    if(cambio.x > 0)
      dir = derecha;
    else if(cambio.x < 0)
      dir = izquierda;
  }
  @Override
  void seleccionarImagenActual(){
    if(dir == derecha){
      if(enPiso)
        actual = irDer;
      else
        actual = moverDer;
    }
    else if(dir == izquierda){
      if(enPiso)
        actual = irIzq;
      else
        actual = moverIzq;
    }
  }
}
