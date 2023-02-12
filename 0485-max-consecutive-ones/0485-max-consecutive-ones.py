class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sumi = 0
        maxi = 0
        for i in nums:
            sumi += i
            maxi = max(maxi,sumi)
            if i == 0:
                sumi = 0
        return maxi
            
        