class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            # Check if there's at least one duplicate character
            if len(set(s)) < len(s):
                return True
            else:
                return False
        
        # Find all indices where s and goal differ
        pairs = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                pairs.append((s[i], goal[i]))
                
        # There must be exactly 2 differing pairs and they must be swappable
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]