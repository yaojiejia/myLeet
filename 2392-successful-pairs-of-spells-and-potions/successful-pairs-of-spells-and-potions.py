from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        
        for i in range(len(spells)):   
            spell = spells[i]

            lp = 0
            rp = len(potions) - 1
            while lp <= rp:
                mid = (lp + rp) // 2
                if spell * potions[mid] < success:   
                    lp = mid + 1
                else:
                    rp = mid - 1

            res.append(len(potions) - lp) 
        return res
