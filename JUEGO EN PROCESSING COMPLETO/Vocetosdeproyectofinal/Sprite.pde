class Sprite
{
  PImage img;
  PVector center, cambio, tamano;
  int tipo, num;
  Sprite(PImage archivo, float x, float y)
  {
   img = archivo;
   tamano = new PVector(img.width,img.height);
   center = new PVector(x,y);
   cambio = new PVector(0,0);
   tipo = 0;
   num = 0;
  }
  Sprite(PImage archivo, int pared)
  {
   img = archivo;
   tamano = new PVector(img.width,img.height);
   center = new PVector(0,0);
   cambio = new PVector(0,0);
   tipo = 0;
   num = pared;
  }
  Sprite(float x, float y)
  {
    img = new PImage();
    tamano =new PVector(0,0);
    center = new PVector(x,y);
    cambio = new PVector(0,0);
    tipo = 0;
  }
  void mostrar()
  {
    image(img,center.x,center.y);
  }
  void mover()
  {
    center.x += cambio.x;
    center.y += cambio.y;
  }
  void setLeft(float left)
  {
    center.x = left + tamano.x/2;
  }
  float getleft()
  {
    return center.x - tamano.x/2;
  }
  void setRight(float right)
  {
    center.x = right - tamano.x/2;
  }
  float getRight()
  {
    return center.x + tamano.x/2;
  }
  void setTop(float top)
  {
    center.y = top + tamano.y/2;
  }
  float getTop()
  {
    return center.y - tamano.y/2;
  }
  void setBottom(float bottom)
  {
    center.y = bottom - tamano.y/2;
  }
  float getBottom()
  {
    return center.y + tamano.y/2;
  }
}
