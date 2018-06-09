public class Figura
{
  protected int x;
  protected int y;
  
  public Figura(int x, int y)
  {
    this.x=x;
    this.y=y;
  }
  
  public void setX(int x)
  {
     this.x=x;
  }
  public int getX()
  {
    return x;
  }
  public void setY(int y)
  {
     this.y=y;
  }
  public int getY()
  {
    return y;
  }
  public String getInformacion()
  {
   return "\nPosición en X: "+x+"\nPosición en Y: "+y;
  }
}