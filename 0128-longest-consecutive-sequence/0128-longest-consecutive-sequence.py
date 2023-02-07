class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count = 1
        maxi = 1
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i + 1]:
                continue
            if nums[i] + 1 != nums[i + 1]:
                count = 0
            count += 1
            maxi = max(count,maxi)
        return maxi
            
                
                
        