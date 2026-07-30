class Solution {
    public int dominantIndex(int[] nums) {
       int l=nums.length;
       int max =nums[0];
       int ind=0; 
       for(int i=1;i<l;i++){
        if(nums[i]>max){
            max=nums[i];
            ind=i;
        }
       }
       for(int j=0;j<l;j++){
        if(max==nums[j]){
            continue;
        }
        if(nums[j]*2 >max){
            return -1;
        }
       }
       return ind;
    }
}