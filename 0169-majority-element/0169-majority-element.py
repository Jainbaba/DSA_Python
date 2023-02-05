class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2] if nums.count(nums[len(nums)//2]) > len(nums)//2 else -1