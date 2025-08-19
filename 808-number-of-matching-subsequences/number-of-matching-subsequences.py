class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Create a dictionary to map each character in s to its indices
        char_to_indices = defaultdict(list)
        for index, char in enumerate(s):
            char_to_indices[char].append(index)
        
        def is_subsequence(word):
            curr_pos = -1
            
            for c in word:
                indices = char_to_indices[c]
                # Use binary search to find the first index > curr_pos
                i = bisect_right(indices, curr_pos)
                
                # If i = length of indices, it means there are no valid positions left
                if i == len(indices):
                    return False
                
                curr_pos = indices[i]

            # If all characters are matched, return True
            return True
        
        return sum(1 for word in words if is_subsequence(word))