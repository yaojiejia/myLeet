class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        String[] parts = s.split("\\s+");;
        String reverse = "";
         for (int i = parts.length - 1; i > 0; i--) {
            // Append the current word and a space to the output
            reverse += parts[i] + " ";
        }
       
        
        
        return reverse + parts[0];

    }
}