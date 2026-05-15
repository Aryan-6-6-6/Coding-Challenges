    import java.util.Scanner;

    class compoundInterest {
        public static void main(String[] argv) {
        
        Scanner input = new Scanner(System.in); 
        
        // User input for amount
        System.out.print("Enter Principal Amount : ");
        int p = input.nextInt();
        
        // user input for Rate of Interest
        System.out.print("Enter Rate of Interest : ");
        double r = input.nextFloat();
        
        // Compounded annually
        System.out.print("Enter the number of times the interest is compounded per year: ");
        double n = input.nextFloat();
        
        System.out.print("Enter time(in years) : ");
        double t = input.nextFloat();
        
        // Compound Amount Formula
        double A = p*Math.pow((1 + ((r/100)/n)),n * t);
        System.out.printf("The amount after %.2f years is : %.3f\n",t,A);
        
        // Compound Interest Formula
        double C = A - p;
        System.out.printf("The interest after %.2f years is : %.3f",t,C);
            
        input.close();

    }
        
}