class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sumi = 0
        maxi = 0
        for i in nums:
            sumi += i
            if  i == 0:
                maxi = max(maxi,sumi)
                sumi = 0
        maxi = max(maxi,sumi)
        return maxi
            
        