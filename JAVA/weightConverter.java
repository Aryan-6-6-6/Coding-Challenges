import java.util.Scanner;

class weightConverter {
	public static void main(String[] argv) {
    
    int choice;
    double kg,lb;
    // Including Object
    Scanner input = new Scanner(System.in);
    
    System.out.println("Simple Weight Conerter ");
    22222222222222222222222222222222222222222222222
    // Options
    System.out.println("1 - Kilograms(kgs) \n 2 -Pounds(lbs)");
    
    // User Input
    System.out.print("Enter option : ");
    choice = input.nextInt();
    
    switch(choice) {
		
        case 1:
        System.out.print("Enter weight in kgs : ");
        kg = input.nextFloat();
        lb = kg * 2.20462;  // Conversion factor
        System.out.println("Your weight in pounds (lbs) is: " + lb);
        break;

        case 2:
        System.out.print("Enter weight in pounds: ");
        lb = input.nextDouble();
           kg = lb / 2.20462;  // Conversion factor
        System.out.println("Your weight in kilograms (kg) is: " + kg);
        break;

        default:
        System.out.println("Invalid choice! Please select a valid option.");
        break;
        }
    }
}