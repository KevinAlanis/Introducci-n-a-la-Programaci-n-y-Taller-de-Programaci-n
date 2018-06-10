 import javax.swing.JOptionPane;
 public class Menu
 {
   Figura figura;
   Circulo circulo;
   Rectangulo rectangulo;
   int opcion=0;
   String valorLeido;
   int alto, ancho, r, x, y;
   
   public Menu()
   {
     do{
       opcion=Integer.parseInt(JOptionPane.showInputDialog("*****Menú*****\n"+
                                                           "1.Calcular área de un círculo"+
                                                           "\n2.Calcular área de un rectangulo"+
                                                           "\n3.Salir"));
       
       switch(opcion)
       {
         
         case 1:
           x=Integer.parseInt(JOptionPane.showInputDialog("Ingrese la posición en X"));
           y=Integer.parseInt(JOptionPane.showInputDialog("Ingrese la posición en Y"));
           r=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor del radio"));
           circulo=new Circulo(x, y, r);
           JOptionPane.showMessageDialog(null,circulo.calcularArea());
           JOptionPane.showMessageDialog(null,"El valor del área es: "+circulo.getInformacion());
           
           break;
           
         case 2:
           x=Integer.parseInt(JOptionPane.showInputDialog("Ingrese la posición en X"));
           y=Integer.parseInt(JOptionPane.showInputDialog("Ingrese la posición en Y"));
           ancho=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor del ancho"));
           alto=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor del alto"));
           rectangulo=new Rectangulo(x, y, alto, ancho);
           JOptionPane.showMessageDialog(null,"El valor del área es: "+rectangulo.calcularArea());
           JOptionPane.showMessageDialog(null,rectangulo.getInformacion());
           
           break;
           
         case 3:
           JOptionPane.showMessageDialog(null,"Hasta pronto. Gracias por utilizar el programa.");
           break;
         default: JOptionPane.showMessageDialog(null,"Opcion inválida.");
         
       }
     }while(opcion!=3);
   }
   
   public static void main(String arg[])
   {
     Menu menu=new Menu();
   }
 }