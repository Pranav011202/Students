class Solution {
    public:
        void moveZeroes(vector<int>& nums) {
            //algorithm - Two pointers 
            // first pointer would be traversing the array and the second pointer would be pointing to the zero 
            int j = -1;
            //placing the jth pointer on the first zero we have encountered 
            for(int i=0 ; i<nums.size() ; i++){
                if(nums[i] == 0){
                    j = i;
                    break;
                }
            }
            if(j!= -1){
                //iterate from i=j+1 to the end of the array 
            for(int i=j+1 ; i<nums.size() ; i++){
                if(nums[i] != 0){
                    swap(nums[i] , nums[j]);
                    j++;
                }
            }
            }
            
        }
    };