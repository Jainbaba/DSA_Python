class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(0,len(nums)):
            sum1 = target - nums[i]
            if sum1 in hashMap:
                return [hashMap[sum1],i]
            hashMap[nums[i]] = i
                
            
        
            

        