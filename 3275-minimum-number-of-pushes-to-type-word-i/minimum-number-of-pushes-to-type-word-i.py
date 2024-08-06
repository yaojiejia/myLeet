class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        res = 0
        if len(count) <= 8:
            return len(word)
        sort = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        print(sort)
        tracker = 0
        for c in sort:
            tracker += 1
            res += sort[c] * math.ceil(tracker/8)
        return res