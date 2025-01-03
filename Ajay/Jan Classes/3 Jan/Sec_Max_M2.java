import java.util.Scanner;
public class Main{
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the size of the  given array :- ");
        int n = sc.nextInt();
// declaring the array
        int[] nums = new int[n];
// populating the array
        for(int i=0 ; i<n ; i++){
            nums[i] = sc.nextInt();
        }
        
// Second Maximum - First step is to find maximum then find sec max 
            int max=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]> max){
                 max = nums[i];
            }
        }
        
        System.out.println("The largest is " + max);
        
        // find the second max 
        int second_max = 0 ;
        
        for(int i=0 ; i<nums.length ; i++){
            if(nums[i] > second_max && nums[i] != max){
                second_max = nums[i];
            }
        }
        
        System.out.println("The second largest element is "+ second_max);
      
         
           }
    
}
            
