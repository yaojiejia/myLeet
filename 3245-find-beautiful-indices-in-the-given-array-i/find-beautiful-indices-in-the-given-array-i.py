class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        a_idx = []
        b_idx = []

        for i in range(len(s) - len(a) + 1):
            if s[i:i+len(a)] == a:
                a_idx.append(i)
        for i in range(len(s) - len(b) + 1):
            if s[i:i+len(b)] == b:
                b_idx.append(i)

        ans = set()
        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(a_idx) and ptr2 < len(b_idx):
            if abs(a_idx[ptr1] - b_idx[ptr2]) <= k:
                ans.add(a_idx[ptr1])
                ptr1 += 1
            elif a_idx[ptr1] < b_idx[ptr2]:
                ptr1 += 1
            else:
                ptr2 += 1

        return sorted(ans)
