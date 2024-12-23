import java.util.Scanner;

public class Assignment{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the size of the array ");
        int n = sc.nextInt();

        int[] nums = new int[n];

        for(int i=0 ; i<n ; i++){
            nums[i] = sc.nextInt();
        }

        System.out.println("Enter the target Value");
        int target = sc.nextInt();

        for(int i=0 ; i< nums.length ; i++){
            if(nums[i] == target){
                System.out.println(i);
                break;
            }
        }
    }
}