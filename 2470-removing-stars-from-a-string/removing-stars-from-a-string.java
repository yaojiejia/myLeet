import java.util.Stack;

class Solution {
    public String removeStars(String s) {
        Stack<Integer> s1 = new Stack<Integer>(); 
        for (int i = 0; i < s.length(); i++) {
            if ( s.charAt(i) != '*') {
                s1.push(i);
            }
            else if( s.charAt(i) == '*'){
                s1.pop();
            }
        }
        
        StringBuilder result = new StringBuilder();
        while (!s1.isEmpty()) {
            result.append(s.charAt(s1.pop()));
        }
        return result.reverse().toString();
    }
}
