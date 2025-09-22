class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        res = 0
        hamsters = list(hamsters)

        for i, x in enumerate(hamsters):
            if x == 'H':
                # Already covered by a bucket
                if (i-1 >= 0 and hamsters[i-1] == 'B') or (i+1 < n and hamsters[i+1] == 'B'):
                    continue

                # Prefer placing bucket on the right if possible
                if i+1 < n and hamsters[i+1] == '.':
                    hamsters[i+1] = 'B'
                    res += 1
                # Otherwise place bucket on the left
                elif i-1 >= 0 and hamsters[i-1] == '.':
                    hamsters[i-1] = 'B'
                    res += 1
                else:
                    return -1

        return res
