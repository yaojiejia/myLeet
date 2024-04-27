class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int lp = 0;
        int rp = nums.length - 1;
        int count = 0;
        while(lp < rp){
            int sum = nums[lp] + nums[rp];
            if(sum == k){
                count++;
                lp++;
                rp--;
            } else if(sum>k){
                rp--;
            }
            else{
                lp++;
            }
        }
        return count;
    }
}