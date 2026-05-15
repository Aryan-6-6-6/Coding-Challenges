import java.util.Scanner;

class quiz_guessGame {
    public static void main(String[] argv) {

        //JAVA QUIZ
        Scanner input = new Scanner(System.in);
        String[] questions = {"Who is the founder of Microsoft? ",
                                "Who is the founder of Amazon",
                                "Who Developed C Language?",
                                "Who Developed Python?",
                                "What is the Full Form of DSA?"};

        // Options
        String[][] options = {
            {"1. Bill Gates", "2. Steve Jobs", "3. Mark Zuckerberg", "4. Larry Page"},
            {"1. Elon Musk", "2. Jeff Bezos ", "3. Sundar Pichai", "4. Warren Buffet"},
            {"1. Dennis Ritchie", "2. Bjarne Stroustrup", "3. Guido van Rossum", "4. James Gosling"},
            {"1. Guido van Rossum", "2. Dennis Ritchie", "3. Tim Berners-Lee", "4. Brendan Eich"},
            {"1. Data Science Algorithm", "2. Data Structures and Algorithms", "3. Digital System Architecture", "4. Distributed Systems Application"}
        };
        // Correct answers (indices)
        int[] correctAnswers = {1, 2, 1, 1, 2};

        // Welcome Message
        System.out.print("----------------------------");
        System.out.print("Welcome to Simple Guessing Game!");

        int count = 0;
        int guess;
        int points = 0;
        
        while(count != 5) {
            for(int i = 0; i< questions.length;i++) {
                System.out.print("----------------------------\n");
                System.out.println(questions[i]);
                for(int j = 0; j< options[i].length; j++) {
                    System.out.println(options[i][j]);
                }
            System.out.print("Choose any one option : ");
            guess = input.nextInt();
            if(guess == correctAnswers[i])
                points++;

            count++;

            }

        } 

      // Final score
    System.out.println("\n----------------------------");
    System.out.println("Quiz Completed!");
    System.out.println("Your total score is: " + points + "/" + questions.length);
    System.out.println("----------------------------");

      input.close(); // Close the scanner
    }
}