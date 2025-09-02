class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # straight line means same slope across the coordinates

        def calculateSlope(x1, x2):
            if x2[0] - x1[0] == 0:
                return float('inf')
            return (x2[1] - x1[1]) / (x2[0] - x1[0])
        slope = calculateSlope(coordinates[0], coordinates[1])

        for i in range(1, len(coordinates)):
            curr_slope = calculateSlope(coordinates[i], coordinates[i-1])
            if curr_slope != slope:
                return False
        
        return True