class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ma = 0
        mi = float('inf')
        nums.sort()
        for num in nums:
            t = max(num)
            ma = max(ma, t)
            t = min(num)
            mi = min(mi,t)
        
        cars = [0]*(ma)

        for num in nums:
            for i in range(num[0]-1, num[1]):
                cars[i] = 1
        return len(cars) - cars.count(0)