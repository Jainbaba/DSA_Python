class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0,len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while(l<r):
                sumi = nums[i] + nums[l] + nums[r]
                if sumi < 0:
                    l += 1
                if sumi > 0:
                    r -= 1
                if sumi == 0:
                    res.append([nums[l],nums[r],nums[i]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        return res
        
             
            
            
        
                    
        

                
                
                
        