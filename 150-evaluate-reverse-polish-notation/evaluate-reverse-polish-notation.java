import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<String> s1 = new Stack<String>();
        int value = 0;
        for(int i = 0; i < tokens.length; i++){
            if(!tokens[i].equals("+") && !tokens[i].equals("-") && !tokens[i].equals("*") && !tokens[i].equals("/")){
                s1.push(tokens[i]);
            }
            else{
                int n1 = Integer.parseInt(s1.pop());
                int n2 = Integer.parseInt(s1.pop());
                if(tokens[i].equals("+")){
                    value = n2 + n1;
                    s1.push(Integer.toString(value));
                }
                else if(tokens[i].equals("/")){
                    value = n2 / n1;
                    s1.push(Integer.toString(value));
                }
                else if(tokens[i].equals("-")){
                    value = n2 - n1;
                    s1.push(Integer.toString(value));
                }
                else if(tokens[i].equals("*")){
                    value = n2 * n1;
                    s1.push(Integer.toString(value));
                }
            }
        } 
        return Integer.parseInt(s1.pop());       
    }
}
