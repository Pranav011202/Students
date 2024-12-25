import java.util.Scanner;
public class Assignment{
    //linear search
    public int linearSearch(int[]nums , int target){
            for(int i=0 ; i<nums.length ; i++){
                if(nums[i] == target){
                    return i;
                }
            }
            return -1;
    }
    //main function
    public static void main(String[] args){
        //object creation of scanner class
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the size of the array");
        int n = sc.nextInt();
        //array declaration
        int[] nums = new int[n];

        //populating the array
        for (int i=0 ; i<n ; i++){
            nums[i] = sc.nextInt();
        }
        System.out.println("Enter the target value");
        int target = sc.nextInt();
        Assignment ans = new Assignment();

        int result = ans.linearSearch(nums,target);

        System.out.println("The index is " + result);

    }
}