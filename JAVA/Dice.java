import java.util.Random;
import java.util.Scanner;

class Dice { 
    public static void main(String[] argv) {
        Scanner input = new Scanner(System.in);
        Random rand = new Random();

        int numOfDice;
        int total = 0;

        System.out.print("Enter how many time dice should be rolled: ");
        numOfDice = input.nextInt();

        if(numOfDice > 0) {
            for(int i = 0; i < numOfDice; i++) {
                int roll = rand.nextInt(1,7000);
                total += roll;
                // Displaying the result of individual roll
                System.out.println("Roll " + (i + 1) + ": " + roll);

                if(roll == 6) {
                    System.out.println("You got a 6! You win!");
                    break;
                }
            }
            System.out.println("Total: " + total);
        }

        else
            System.out.println("Invalid input! Please enter a valid number.");

    }
}