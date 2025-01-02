// Write a program to:

// Print the sum of negative numbers,
// Print the sum of positive odd numbers, and
// Print the sum of positive even numbers
// from a list of numbers entered by the user.
// The list terminates when the user enters zero (0).

import java.util.Scanner;

public class Assignment{
    public static void main(String[] args) {
        //Created a scanner object to take the user input
        Scanner sc = new Scanner(System.in);

        int sumNegative = 0;
        int sumPositiveOdd = 0;
        int sumPositiveEven = 0 ;

        System.out.println("Enter numbers (Enter 0 to step) ");
        while(true){
            int number = sc.nextInt();
            // if the number is 0 then break the loop
            if(number == 0){
                break;
            }
            //check if the number is negative
            else if(number <0){
                sumNegative += number;
            }
            // check if the number is positive and even
            else if(number>0 && number % 2 == 0){
                sumPositiveEven += number;
            }
            else if(number>0 && number % 2 != 0){
                sumPositiveOdd += number;
            }
        }
        System.out.println("Sum of negative numbers " + sumNegative);
        System.out.println("Sum of positive even numbers "+ sumPositiveEven);
        System.out.println("Sum of positive odd numbers "+ sumPositiveOdd);

    }
}