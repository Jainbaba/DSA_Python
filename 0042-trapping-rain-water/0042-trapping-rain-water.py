class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right =  [height[n-1]]
        left = [height[0]]
        for i in range(1,n):
            left.append(max(height[i],left[-1]))
            right.append(max(height[n-1-i],right[-1]))
        units = 0
        for i in range(0,n):
            units += min(left[i],right[n-1-i]) - height[i]
        return units
        