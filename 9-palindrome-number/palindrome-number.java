class Solution {
    public boolean isPalindrome(int x) {
        String text = String.valueOf(x);
        if(text.length()<=0){
            return false;
        }
        int left = 0;
        int right = text.length()-1;
        while(left < right){
            if(text.charAt(left)!=text.charAt(right)){
                return false;
            }
            else{
                left++;
                right--;
            }
        }
        return true;
    }
}