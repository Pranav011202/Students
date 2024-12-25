import  java.util.Scanner;
public class Assignment{
    public int largestElement(int[] nums){
        int max = Integer.MIN_VALUE;
        for(int i=0 ; i<nums.length ; i++){
            if(nums[i] > max){
                max = nums[i];
            }
        }
        return max;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        //Take size of array as input
        System.out.println("Enter the size of array");
        int n = sc.nextInt();

        //array declaration

        int[] nums = new int[n];

        //populate the array
        for(int i=0 ; i<n ; i++){
            nums[i] = sc.nextInt();
        }

        Assignment ans = new Assignment();
        int res = ans.largestElement(nums);

        System.out.println(res);

    }
}