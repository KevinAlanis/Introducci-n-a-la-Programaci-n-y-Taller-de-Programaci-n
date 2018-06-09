import java.lang.Math;
public class Rectangulo extends Figura
{
  protected int alto;
  protected int ancho;
  
  public Rectangulo(int x, int y, int alto, int ancho)
  {
    super(x, y);
    this.alto=alto;
    this.ancho=ancho;
  }
  
  public void setAlto(int alto)
  {
    this.alto=alto;
  }
  public int getAlto()
  {
    return alto;
  }
  public void setAncho(int ancho)
  {
    this.ancho=ancho;
  }
  public int getAncho()
  {
    return ancho;
  }
  
  public double calcularArea()
  {
    return alto*ancho;
  }
  public String getInformacion()
  {
    return super.getInformacion()+"\nEl valor del alto: "+alto+"\nEl valor del ancho: "+ancho+"\nEl área del rectangulo es: "+calcularArea();
  }
}