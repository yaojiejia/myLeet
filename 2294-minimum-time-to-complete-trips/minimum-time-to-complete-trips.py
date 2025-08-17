class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 1 2 3 4 5
        # the minimum time to complete totalTrips is time[0] * totalTrips
        # sort time first

        time.sort()
        lp = 1
        rp = time[0] * totalTrips

        while lp <= rp:
            mid_time = (rp + lp) // 2
            curr_trip = 0
            for t in time:
                curr_trip += mid_time // t
            if curr_trip < totalTrips:
                lp = mid_time + 1
            else:
                rp = mid_time - 1
        return lp