import javax.swing.JOptionPane;
public class MultiplicarMatrices
{
  int matriz1[][], matriz2[][], matriz3[][];
  int filas1, columnas1, filas2, columnas2, opcion;
  public MultiplicarMatrices()
  {
      filas1=Integer.parseInt(JOptionPane.showInputDialog("Digite la cantidad de filas de la matriz 1"));
      columnas1=Integer.parseInt(JOptionPane.showInputDialog("Digite la cantidad de columnas de la matriz 1"));
      matriz1=new int[filas1][columnas1];
      filas2=Integer.parseInt(JOptionPane.showInputDialog("Digite la cantidad de filas de la matriz 2"));
      columnas2=Integer.parseInt(JOptionPane.showInputDialog("Digite la cantidad de columnas de la matriz 2"));
      matriz2=new int[filas2][columnas2];
      matriz3=new int[filas1][columnas2];
      
    do{
     opcion=Integer.parseInt(JOptionPane.showInputDialog("****Menú:****\n1.Llenar la matriz 1."+"\n2.Imprimir matriz 1."+
                                                         "\n3.Llenar la matriz 2."+"\n4.Imprimir matriz 2"+
                                                         "\n5.Multiplicar matriz 1 con matriz 2 y almacenarlo en una matriz 3."+
                                                         "\n6.Imprimir matriz 3"+"\n7.Salir"));
     switch(opcion)
     {
       case 1:
         JOptionPane.showMessageDialog(null,"Ingrese los valores 1 a la vez para llenar las filas y columnas de la matriz.");
         llenarMatriz1();
         break;
         
         case 2:
           imprimirMatriz1();
         break;
         
         case 3:
           JOptionPane.showMessageDialog(null,"Ingrese los valores 1 a la vez para llenar las filas y columnas de la matriz.");
           llenarMatriz2();
         break;
         
         case 4:
           imprimirMatriz2();
         break;
         
         case 5:
           llenarMatriz3(matriz1, matriz2, matriz3);
         break;
       case 6:
         imprimirMatriz3();
         break;
         
       case 7:
         JOptionPane.showMessageDialog(null,"Fin del programa.");
         break;
         
       default:JOptionPane.showMessageDialog(null,"La opcion no es válida.");
     }
      
    }while(opcion!=7);
  }
 //------------------------------------------------------------------------------------------------------------------------------------------------------------- 
  public void llenarMatriz1()
    //tamaño de las filas matriz.lenght
    //tamaño de las columnas matriz[0].length
  {
    for(int fila1=0;fila1<matriz1.length;fila1++)
    {
      for(int columna1=0;columna1<matriz1[0].length;columna1++)
      {
        matriz1[fila1][columna1]=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor deseado para ir formando la matriz"));
      }
    }
    JOptionPane.showMessageDialog(null,"La matriz se lleno correctamente.");
  }
  //------------------------------------------------------------------------------------------------------------------------------------------------------------ 
  public void imprimirMatriz1()
  {
    String valores="";
    for(int fila1=0;fila1<matriz1.length;fila1++)
    {
      for(int columna1=0;columna1<matriz1[0].length;columna1++)
      {
        valores+=" "+matriz1[fila1][columna1];
      }
      valores+="\n";
    }
    JOptionPane.showMessageDialog(null,"La matriz 1 es:\n"+valores);
  }
 //------------------------------------------------------------------------------------------------------------------------------------------------------------  
  public void llenarMatriz2()
    //tamaño de las filas matriz.lenght
    //tamaño de las columnas matriz[0].length
  {
    for(int fila2=0;fila2<matriz2.length;fila2++)
    {
      for(int columna2=0;columna2<matriz2[0].length;columna2++)
      {
        matriz2[fila2][columna2]=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor deseado para ir formando la matriz"));
      }
    }
    JOptionPane.showMessageDialog(null,"La matriz se lleno correctamente.");
  }
 //------------------------------------------------------------------------------------------------------------------------------------------------------------  
  public void imprimirMatriz2()
  {
    String valores="";
    for(int fila2=0;fila2<matriz2.length;fila2++)
    {
      for(int columna2=0;columna2<matriz2[0].length;columna2++)
      {
        valores+=" "+matriz2[fila2][columna2];
      }
      valores+="\n";
    }
    JOptionPane.showMessageDialog(null,"La matriz 2 es:\n"+valores);
  }
 //-------------------------------------------------------------------------------------------------------------------------------------------------------------
  public void llenarMatriz3(int matriz1[][], int matriz2[][], int matriz3[][])
    //tamaño de las filas matriz.lenght
    //tamaño de las columnas matriz[0].length
  {
    for(int fila3=0;fila3<matriz3.length;fila3++)
    {
      for(int columna3=0;columna3<matriz3[0].length;columna3++)
      {
        for(int columna=0; columna<matriz1[0].length;columna++)
        {
        matriz3[fila3][columna3]+=matriz1[fila3][columna]*matriz2[columna][columna3];
        }
      }
    }
    JOptionPane.showMessageDialog(null,"La matriz se lleno correctamente con los productos de las matrices 1 y 2.");
  
  }
 //------------------------------------------------------------------------------------------------------------------------------------------------------------  
  public void imprimirMatriz3()
  {
    String valores="";
    for(int fila3=0;fila3<matriz3.length;fila3++)
    {
      for(int columna3=0;columna3<matriz3[0].length;columna3++)
      {
        valores+=" "+matriz3[fila3][columna3];
      }
      valores+="\n";
    }
    JOptionPane.showMessageDialog(null,"La matriz 3 es:\n"+valores);
  }
  //------------------------------------------------------------------------------------------------------------------------------------------------------------ 
  public static void main(String arg[])
  {
    MultiplicarMatrices multiplicarMatrices=new MultiplicarMatrices();
  }

}