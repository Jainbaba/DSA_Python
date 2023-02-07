class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        count = 1
        maxi = 1
        for i in nums:
            if i-1 not in nums:
                count = 0
                while i+count in nums:
                    count+= 1
                maxi = max(count,maxi)
        return maxi
            
                
                
        