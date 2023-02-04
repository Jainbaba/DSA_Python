class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while(i > -1):
            if nums[i] < nums[i+1]:
                for j in range(len(nums)-1,i,-1):
                    if nums[i] < nums[j]:
                        nums[i],nums[j] = nums[j],nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        return nums
            i-=1
        return nums.reverse()
                        
            
            
    