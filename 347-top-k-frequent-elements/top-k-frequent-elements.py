from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in the list
        count = Counter(nums)
        
        # Get the most common elements as a list of tuples
        most_common_elements = count.most_common()
        
        # Initialize an empty list to store the result
        res = []
        
        # Loop through the most common elements and add the first k elements to res
        for i in range(k):
            res.append(most_common_elements[i][0])
        
        return res
