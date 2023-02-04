class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currProd = 1
        maxi = float("-inf")
        for num in nums:
            currProd *= num
            maxi = max(maxi,currProd)
            if currProd == 0:
                currProd = 1
            
            
        currProd = 1
        for num in nums[::-1]:
            currProd *= num
            maxi = max(maxi,currProd)
            if currProd == 0:
                currProd = 1
           
        return maxi

        