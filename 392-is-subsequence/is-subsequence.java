class Solution {
    public boolean isSubsequence(String s, String t) {
        int position = -1;
        for(int i = 0; i < s.length(); i++){
            boolean found = false;
            for(int j = position+1; j < t.length(); j++){
                if(s.charAt(i) == t.charAt(j)){
                    found = true;
                    position = j;
                    break;
                }
            
        }
        if(!(found)) return false;
    }
    return true;
}
}