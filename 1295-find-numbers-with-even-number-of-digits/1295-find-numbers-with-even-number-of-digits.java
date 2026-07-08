class Solution {
    public int findNumbers(int[] nums) {
     int le=nums.length;
     int e=0;
     for (int i=0;i<le;i++){
        int digits = 0;
        int v=nums[i];
        while (v>0){
           digits += 1;
            v=v/10;
        }
        if (digits % 2 == 0){
           e += 1;
        }
        

     }  
     return e; 
    }
    
}