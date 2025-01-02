// Ques - Design a class named GreenHighTravels to calculate the fare as per the table given below:
// Table in assignment ques 5 

import java.util.Scanner;

public class Assignment{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name");
        String passengerName = scanner.nextLine();

        System.out.println("Enter Distance Travelled (in km): ");
        int distanceTravelled = scanner.nextInt();

        int totalFare = 0;

        if(distanceTravelled <= 20){
            totalFare = distanceTravelled * 40;
        } else if (distanceTravelled <= 60 ){
            totalFare = distanceTravelled * 35;
        } else{
            totalFare = distanceTravelled * 32;
        }

        // Display the details
        System.out.println("\nPassenger Details:");
        System.out.println("Passenger Name: " + passengerName);
        System.out.println("Mode of Journey: Car");
        System.out.println("Distance Travelled: " + distanceTravelled + " km");
        System.out.println("Total Fare: ₹" + totalFare);
    }
}