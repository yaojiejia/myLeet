class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')  # Use a set for O(1) lookups and include uppercase vowels
        l = list(s)
        lp = 0
        rp = len(l) - 1  # Initialize rp to the last valid index

        while lp < rp:
            while lp < rp and l[lp] not in vowels:
                lp += 1
            while lp < rp and l[rp] not in vowels:
                rp -= 1
            if lp < rp:
                l[lp], l[rp] = l[rp], l[lp]  # Swap the vowels
                lp += 1
                rp -= 1

        return "".join(l)

# Example usage
solution = Solution()
result = solution.reverseVowels("hello")
print(result)  # Output should be "holle"
