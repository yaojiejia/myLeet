class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        tCounter = Counter(target)
        aCounter = Counter(arr)
        # tRes = Counter(tCounter)
        # aRes = Counter(aCounter)
        print(tCounter)
        print(aCounter)
        return tCounter == aCounter