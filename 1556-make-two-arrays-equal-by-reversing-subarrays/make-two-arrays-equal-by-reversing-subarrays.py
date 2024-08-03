class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        tCounter = Counter(target)
        aCounter = Counter(arr)
        return tCounter == aCounter