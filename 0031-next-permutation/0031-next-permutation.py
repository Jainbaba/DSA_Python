class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]: 
                nums[i:] = sorted(nums[i:])
                
                for k in range(i, len(nums)):
                    if nums[k] > nums[i-1]:
                        nums[k], nums[i-1] = nums[i-1], nums[k]
                        return nums
        return nums.reverse()