class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        right = points[0][1]
        arrows = 1
        for point in points[1:]:
            if point[0] > right: 
                arrows += 1
                right = point[1]
        return arrows
            

