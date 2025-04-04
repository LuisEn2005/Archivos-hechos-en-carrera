class Fondo{
  PImage mySprite[],bgfondo;
  float sizeSprite;
  Fondo(String name, String tilemap, float size){
    sizeSprite=size;
    mySprite=new LeerArchivo(8,5,tilemap).getHoja();
    suelo=new ArrayList<Sprite>();
    
    bgfondo=loadImage("EspacioAzul.jpeg");
    crearSuelo(name);
  }
  void mostrar(){
    image(bgfondo,view_x+width/2,height/2-130);
    for(Sprite p: suelo)
      p.mostrar();
  }
  void crearSuelo(String archivo){
    String[] lineas=loadStrings(archivo);
    for(int row=0; row<lineas.length; row++){
      String[] valores=split(lineas[row],";");
      for(int col=0; col<valores.length; col++){
        int num=obtenerNum(valores[col]);
        if(num<13){
          Sprite s=new Sprite(mySprite[num],num);
          s.center.x=sizeSprite/2 + col*sizeSprite;
          s.center.y=sizeSprite/2 + row*sizeSprite;
          suelo.add(s);
        }
      }
    }
  }
  int obtenerNum(String txt){
    int num=0;
    num=Integer.valueOf(txt);
    return num;
  }
}
