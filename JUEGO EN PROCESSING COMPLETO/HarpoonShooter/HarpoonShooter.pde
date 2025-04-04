final static int normal=0;
final static int derecha=1;
final static int izquierda=2;
final static int tampixel=4;
final static int tamcuadricula=tampixel * 7 + 5;
final static float gravedad=0.6;
final static float vel=6;
color colortexto = color(160,90,190);
int direccion=1;
int delaydisparo=0;
int puntos=0;
int puntajemax=2750;
Boolean Disparar=true;
float view_x=0;
float view_y=0;
PImage[] personaje;
ArrayList<Sprite> suelo;
ArrayList enemigos = new ArrayList();
ArrayList balas = new ArrayList();
Personaje player;
Fondo Escenario;
void setup(){
  size(700,511);
  imageMode(CENTER);
  personaje=new LeerArchivo(10,3,"personaje default.png").getHoja();
  player=new Personaje(personaje[0]);
  player.center.x=350;
  player.center.y=450;
  Escenario=new Fondo("Escenario.csv","Bloques.png",32);
  GenEnemigos();
}

void draw(){
  background(255);
  jugar();
  Puntaje();
  findejuego();
  for (int i = 0; i < balas.size(); i++) {
        Balas bala = (Balas) balas.get(i);
        bala.draw();
  }
  for (int i = 0; i < enemigos.size(); i++) {
        Enemigo enemigo = (Enemigo) enemigos.get(i);
        if (enemigo.Afuera() == true) {
            direccion *= (-1);
            break;
        }
    }
  for (int i = 0; i < enemigos.size(); i++) {
        Enemigo enemigo = (Enemigo) enemigos.get(i);
        if (!enemigo.Vivo()) {
            enemigos.remove(i);
        } else {
            enemigo.draw();
        }
    }
}
boolean tocado(Sprite s1,Sprite s2){
  boolean tocarX = s1.getRight() <= s2.getLeft() || s1.getLeft() >= s2.getRight();
  boolean tocarY = s1.getBottom() <= s2.getTop() || s1.getTop() >= s2.getBottom();
  if(tocarX || tocarY)
    return false;
  else{
    if(s2.num==13 && ((Personaje)s1).estado==0)
      return false;
  }
  return true;
}

ArrayList<Sprite> tocandoLista(Sprite s, ArrayList<Sprite> lista){
  ArrayList<Sprite> listaTocada=new ArrayList<Sprite>();
  for(Sprite p:lista){
    if(tocado(s,p))
      listaTocada.add(p);
  }
  return listaTocada;
}

void resolverColision(Sprite s, ArrayList<Sprite> lista){
  s.cambio.y+=gravedad;
  s.center.y+=s.cambio.y;
  ArrayList<Sprite> colLista = tocandoLista(s,lista);
  if(colLista.size()>0){
    Sprite colision=colLista.get(0);
    if(s.cambio.y>0)
      s.setBottom(colision.getTop());
    else if(s.cambio.y<0)
      s.setTop(colision.getBottom());
    s.cambio.y=0;  
  }
  s.center.x+=s.cambio.x;
  colLista=tocandoLista(s,lista);
  if(colLista.size()>0){
    Sprite colision=colLista.get(0);
    if(s.cambio.x>0)
      s.setRight(colision.getLeft());
    else if(s.cambio.x<0)
      s.setLeft(colision.getRight());
    s.cambio.x=0;
  }
}

boolean estaEnSuelo(Sprite s, ArrayList<Sprite> pared){
  s.center.y+=5;
  ArrayList<Sprite> colLista=tocandoLista(s,pared);
  s.center.y-=5;
  if(colLista.size()>0)
    return true;
  else
    return false;
}
void findejuego(){
  if (puntos == puntajemax){
    text("GameOver",width/2-55,height/2-35);
    fill(colortexto);
    player.center.x = 350;
    player.center.y = 400;
  }
}
void Puntaje(){
  fill(colortexto);
  text("Puntos: " + String.valueOf(puntos),10,40);
  textSize(40);
}
void GenEnemigos() {
    for (int i = -1;i<width/tamcuadricula/2;i++) {
        for (int j = 0; j<5;j++) {
            enemigos.add(new Enemigo(i*50, j*30+50));
        }
    }
}
void jugar(){
  Escenario.mostrar();
  player.mostrar();
  player.actualizar();
  resolverColision(player,suelo);
}
void keyPressed(){
  if(keyCode==RIGHT)
    player.cambio.x=vel;
  else if(keyCode==LEFT)
    player.cambio.x=-vel;
  else if (keyCode== UP && Disparar){
    balas.add(new Balas(player.center.x,player.center.y));
    Disparar = false;
    delaydisparo = 0;
  }
  delaydisparo++;
  if(delaydisparo >= 30){
    Disparar = true;
  }
  }
  void keyReleased(){
  if(keyCode==RIGHT)
    player.cambio.x=0;
  else if(keyCode==LEFT)
    player.cambio.x=0;
  }
