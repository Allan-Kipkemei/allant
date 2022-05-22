import java.lang.Math;
import java.util.Scanner;
public class Methods {
  public static void main(String[] args) {
    double a,b;//,power, root;
    Scanner moni=new Scanner(System.in);
    System.out.println("capture values of a and b");
    a=moni.nextDouble();
    b=moni.nextDouble();
    // using the sqrt() method
    System.out.println("a raised to power b =" + Math.pow(a,b));
    System.out.println("Square root of a is: " + Math.sqrt(a));
  }
}
