class Solution {
    public int[] runningSum(int[] nums) {
        //in the same array we modify the values
       for(int i = 1; i < nums.length; i++){
           nums[i] = nums[i-1] + nums[i];
       }
       return nums;
    }
}