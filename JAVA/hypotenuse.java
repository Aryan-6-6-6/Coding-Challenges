import java.util.Scanner;

class hypotenuse {
    public static void main(String[] argv) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the base of the triangle: ");
        float base =input.nextFloat();

        System.out.print("Enter the height of the triangle: ");
        float height = input.nextFloat();

        // by default return Mth is double
        float result = (float) Math.sqrt(Math.pow(base,2) + Math.pow(height,2));

        System.out.println("The hypotenuse of the triangle is: " + result);

        
    }

}