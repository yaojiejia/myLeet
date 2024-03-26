import java.util.*;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        for (int asteroid : asteroids) {
            if (asteroid > 0) {
                stack.push(asteroid);
            } else {
                while (!stack.isEmpty() && stack.peek() > 0 && stack.peek() < Math.abs(asteroid)) {
                    stack.pop(); // Destroy asteroids moving to the right with smaller sizes
                }
                if (stack.isEmpty() || stack.peek() < 0) {
                    stack.push(asteroid); // Push the current asteroid if it doesn't collide
                } else if (stack.peek() == Math.abs(asteroid)) {
                    stack.pop(); // Destroy both asteroids if they have the same size
                }
            }
        }
        int[] result = new int[stack.size()];
        for (int i = result.length - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }
        return result;
    }
}
