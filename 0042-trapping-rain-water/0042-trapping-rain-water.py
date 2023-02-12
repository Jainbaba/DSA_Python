class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        right =  [height[n-1]]
        left = [height[0]]
        for i in range(1,n):
            left.append(max(height[i],left[-1]))
            right.insert(0,max(height[n-1-i],right[0]))
        units = 0
        for i in range(0,n):
            units += min(left[i],right[i]) - height[i]
        return units
        