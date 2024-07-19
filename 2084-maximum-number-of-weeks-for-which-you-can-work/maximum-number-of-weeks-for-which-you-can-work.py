class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        milestones.sort()
        s = sum(milestones)
        if milestones[-1] * 2 <= s:
            return s
        return (s - milestones[-1]) *2 + 1