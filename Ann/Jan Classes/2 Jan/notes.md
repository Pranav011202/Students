# Paper discussion 

            import java.util.Scanner;
    public class Solution{
    public static void main(String[] args) {
        //object of scanner class
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number ");
        int n = sc.nextInt();
        int p = n;
        int sum = 0 ;
        while(p>0){
            int last_digit = p % 10;
            sum = sum + last_digit;
            p = p / 10;
        }

        if(n % sum == 0 ){
            System.out.println("Its a Niven Number");
        }
        else{
            System.out.println("It is not a Niven Number");
        }
    }
    }