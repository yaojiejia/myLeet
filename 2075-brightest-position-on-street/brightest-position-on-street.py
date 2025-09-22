class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        events = defaultdict(int)
        for pos, interval in lights:
            events[pos - interval] += 1
            events[pos + interval + 1] -= 1

        brightness = 0
        max_bright = -1
        ans = 0

        for x in sorted(events.keys()):
            brightness += events[x]
            if brightness > max_bright:
                max_bright = brightness
                ans = x

        return ans
