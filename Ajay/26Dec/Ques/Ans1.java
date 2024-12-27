import java.util.Scanner;
public class Solution{
    //method for finding the second largest element
    int secLargest(int[] nums){
        int largest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;

        for(int i=0 ; i<nums.length ; i++){
            if(nums[i]>largest){
                largest = nums[i];
            }
            if(nums[i]>secondLargest && nums[i] != largest){
                secondLargest = nums[i];
            }
        }
        return secondLargest;
    }

    public static void main(String[] args) {
        //Creation of scanner object
        Scanner ajay = new Scanner(System.in);

        System.out.println("Enter the size of the array");
        int n = ajay.nextInt();

        //declaration of the array
        int[] nums = new int[n];

        //populate the array
        for(int i=0 ; i<n ; i++){
            nums[i] = ajay.nextInt();
        }

        Solution ans = new Solution();
        int secondLargest = ans.secLargest(nums);

        System.out.println(secondLargest);

    }
}