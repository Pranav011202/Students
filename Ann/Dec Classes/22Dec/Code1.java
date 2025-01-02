// Write a program to input three numbers (positive or negative).

// If they are unequal, then display the greatest number; otherwise, display that they are equal.
// The program also displays whether the numbers entered by the user are "All positive," "All negative," or "Mixed numbers."

import java.util.*;
public class Assignment {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input of three number
        System.out.println("Enter the first Number");
        int num1 = sc.nextInt();
        System.out.println("Enter the second Number");
        int num2 = sc.nextInt();
        System.out.println("Enter the third Number");
        int num3 = sc.nextInt();

        if(num1 == num2 && num2 == num3){
            System.out.println("ALl the numbers are equal");
        }else{
            int greatest = Math.max(num1,Math.max(num2,num3));
            System.out.println("The greatest number is " + greatest);
        }

        //part 2 of our ques
        if(num1>0 && num2 >0 && num3>0){
            System.out.println("All the numbers are positive");
        } else if(num1<0 && num2<0 && num3<0){
            System.out.println("All the numbers are negative");
        }else{
            System.out.println("Numbers are mixed");
        }
    }
}
