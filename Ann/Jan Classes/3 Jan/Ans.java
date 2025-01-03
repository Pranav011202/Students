import java.util.Scanner;
public class Solution{
    public static void main(String[] args) {
    // create an object of the scanner class
        Scanner sc = new Scanner(System.in);

        //Ask for the name
        System.out.println("Enter the name of the laborer");
        String name = sc.nextLine();

        System.out.println("Enter the number of hours worked in a week");
        int hoursWorked = sc.nextInt();

        int weeklyWage = 0;

        if(hoursWorked<=20){
            weeklyWage = hoursWorked * 50;
        } else if(hoursWorked <= 40 ){
            weeklyWage = (20 * 50 ) + ((hoursWorked - 20 ) * 40);
        } else if(hoursWorked <= 40 ){
            weeklyWage = (20 * 50) + (20 * 40) + ((hoursWorked - 40 )* 50);
        }else{
            weeklyWage = (20 * 50 ) + (20 * 40 ) + (10 * 50 ) + ((hoursWorked - 50) * 60);
        }

        System.out.println("Labour Name " + name);
        System.out.println("Total Hours worked "+ hoursWorked);
        System.out.println("Your weekly wage is " + weeklyWage);
    }
}