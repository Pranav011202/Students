import java.util.Scanner;

public class Solution{

    void rotateArrayByOne(int[] nums){
        int temp = nums[0];
        for(int i=1 ; i<nums.length ; i++){
            nums[i-1] = nums[i];
        }

        nums[nums.length-1] = temp;
    }

    public static void main(String[] args) {
        //object for scanner
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of array");
        int n = sc.nextInt();

        //declare the array
        int[] nums = new int[n];

        //populate the array
        for(int i=0 ; i< nums.length ; i++){
            nums[i] = sc.nextInt();
        }

        Solution ajay = new Solution();

        ajay.rotateArrayByOne(nums);

        System.out.println("The rotated array is ");

       for(int i :nums){
           System.out.println(i);
       }
    }
}