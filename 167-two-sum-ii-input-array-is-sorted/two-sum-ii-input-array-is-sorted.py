class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0 
        rp = len(numbers) - 1

        while lp < rp:
            temp = numbers[lp] + numbers[rp]
            if temp == target:
                return [lp+1,rp+1]
            elif temp < target:
                lp += 1
            else:
                rp -= 1
        return []