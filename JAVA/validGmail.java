import java.util.Scanner;

class validGmail {
    public static void main(String[] argv) {
        Scanner input = new Scanner(System.in);
        
        // User input
        System.out.print("Enter your name : ");
        String name = input.nextLine();
        
        // User input for Email Address
        System.out.print("Enter you email id : ");
        String email = input.nextLine();
        
        int z = email.compareTo("@");
        int x = email.compareTo(".com");
        // Check if Email has '@' and .com
        
            if(z == 0 && x == 0) {
                    System.out.println("Email is Valid");
                }
                
            else 
                System.out.println("Perhaps you forgot \'@\'");
            }
        
        
    
}