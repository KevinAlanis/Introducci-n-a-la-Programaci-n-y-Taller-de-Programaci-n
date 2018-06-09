import javax.swing.JOptionPane;

public class BuscarBinario
{
  public static void main(String args[])
  {
    int lista[]=llenarArray();
    int valor = Integer.parseInt(JOptionPane.showInputDialog("Digite el número a buscar."));
    boolean encontrado = buscar(lista,valor);
    if(encontrado == true){
        JOptionPane.showMessageDialog(null,"El valor fue encontrado: "+ encontrado);
    }
    else{
        JOptionPane.showMessageDialog(null,"El valor no fue encontrado o la lista no se encuentra ordenada "+ encontrado);
    }
   

  }
  
  public static int[] llenarArray()
  {
    int lista[];
    int tamanio, valor=0;
    tamanio=Integer.parseInt(JOptionPane.showInputDialog("Digite el tamaño de la lista."));
    lista=new int[tamanio];
    for (int contador=0;contador<tamanio;contador++)
    {
      valor=Integer.parseInt(JOptionPane.showInputDialog("Digite los valores uno a la vez y en orden para llenar la lista."));
      lista[contador]=valor;
    }
    return lista;
  }
  
  public static boolean buscar(int[] lista, int valor)
   {
    int topeList = lista.length-1;
    int pos;
    boolean encontrado = false;
 
    for(int inicioList=0; inicioList <= topeList; )
    {
      pos = (inicioList+topeList)/2;
      if (valor == lista[pos])
      {
        encontrado = true;
        return encontrado;
      }
      else if (lista[pos] < valor)
      {
        inicioList = pos+1;
      }
      else if (lista[pos] > valor )
      {
        topeList = pos-1;
      }
    }
    return encontrado;
   }
  
}