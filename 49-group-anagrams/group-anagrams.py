from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold sorted string as the key and list of anagrams as values
        anagrams = {}
        
        for s in strs:
            # Sort the string to create a key
            key = tuple(sorted(s))
            
            # If the key doesn't exist, create a new entry in the dictionary
            if key not in anagrams:
                anagrams[key] = []
            
            # Append the original string to the list of anagrams for this key
            anagrams[key].append(s)
        
        # Return the list of grouped anagrams
        return list(anagrams.values())
