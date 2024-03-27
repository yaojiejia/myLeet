class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> l1 = new ArrayList<Boolean>();
        int largest = 0;
        for(int i = 0; i < candies.length; i++){
            if(candies[i] > largest){
                largest = candies[i];
            }
        }
        for(int j = 0; j < candies.length; j++){
            if(candies[j] + extraCandies >= largest){
                l1.add(true);
            }
            else{
                l1.add(false);
            }
        }
        return l1;
    }
}