//Create 4 objects on area and calculate area//
import java.util.Scanner;
public class prac 
{
    public void areaRectangle(double r1, double r2)
    {
        double area1=r1*r2;
        System.out.println("==============================");
        System.out.println("The area of the Rectangle is: "+area1);
        System.out.println("Formula used: length*width ");
        System.out.println("==============================");
    }
    public void areaTriangle(double T1, double T2)
    {
        double area2=T1*T2*(1/2);
        System.out.println("==============================");
        System.out.println("The area of the Triangle is: "+area2);
        System.out.println("Formula used: (1/2) x height x base ");
        System.out.println("==============================");
    }
    public void areaCircle(double c1)
    {
        double area3=3.1416*c1*c1;
        System.out.println("==============================");
        System.out.println("The area of the Circle is: "+area3);
        System.out.println("Formula used: pi x r^2 ");
        System.out.println("==============================");
    }
    public void areaSquare(double s1)
    {
        double area4=s1*s1;
        System.out.println("==============================");
        System.out.println("The area of the Square is: "+area4);
        System.out.println("Formula used: Length x length ");
        System.out.println("==============================");
    }

    public static void main(String[]args)
    {
        Scanner sc=new Scanner(System.in);
        double b,c;
        prac obj= new prac();
        for(int i=0;i<2;i--)
        {
            System.out.println("What task do you want to perform ?");
            System.out.println("[1]Rectangle");
            System.out.println("[2]Triangle");
            System.out.println("[3]Circle");
            System.out.println("[4]Square");
            System.out.print("-->");
            int a=sc.nextInt();
            sc.close();
            if(a==1)
            {
                System.out.println("You have chosen rectangle.");
                System.out.print("Length: ");
                b=sc.nextDouble();
                System.out.print("Width: ");
                c=sc.nextDouble();
                obj.areaRectangle(b,c);
            }
            if(a==2)
            {
                System.out.println("You have chosen Triangle.");
                System.out.print("Height: ");
                b=sc.nextDouble();
                System.out.print("Base: ");
                c=sc.nextDouble();
                obj.areaTriangle(b,c);
            }
            if(a==3)
            {
                System.out.println("You have chosen Circle.");
                System.out.print("Radius: ");
                b=sc.nextDouble();
                obj.areaCircle(b);
            }
            if(a==4)
            {
                System.out.println("You have chosen Square.");
                System.out.print("Length of a single arm: ");
                b=sc.nextDouble();
                obj.areaCircle(b);
            }
            else
            {
                System.out.println("Invalid output.");
            }
        }
        }    
    
}
