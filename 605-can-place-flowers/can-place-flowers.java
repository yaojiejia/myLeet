class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        if(flowerbed.length == 1 && flowerbed[0] != 1){
            count++;
            return count >= n;
        }
        if(flowerbed[0] == 1 && flowerbed.length == 1){
            return count >= n;
        }
        if(flowerbed[0] == 0 && flowerbed[1] == 0){
            count++;
            flowerbed[0] = 1;
            
        }
        if(flowerbed[flowerbed.length-1] == 0 && flowerbed[flowerbed.length-2] == 0){
                count++;
                flowerbed[flowerbed.length-1] = 1;
            
        }
        for(int i = 1; i < flowerbed.length-1; i++){
            if(flowerbed[i] == 0 && flowerbed[i-1] == 0 && flowerbed[i+1] == 0){
                count ++;
                flowerbed[i] = 1;
            }
        }
        return count >= n;
    }
}