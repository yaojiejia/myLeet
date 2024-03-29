class Solution {
    public boolean isSubsequence(String s, String t) {
        int position = -1; // Initialize position to -1
        for(int i = 0; i < s.length(); i++) {
            boolean found = false; // Flag to indicate if character is found
            for(int j = position + 1; j < t.length(); j++) {
                if(s.charAt(i) == t.charAt(j)) {
                    found = true; // Set flag to true if character is found
                    position = j; // Update position
                    break; // Exit inner loop
                }
            }
            if(!found) return false; // If character not found, return false
        }
        return true;
    }
}
