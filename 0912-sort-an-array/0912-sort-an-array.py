class Solution:        
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
    
        left = self.sortArray(nums[:len(nums)//2])
        right = self.sortArray(nums[len(nums)//2:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        arr = []
        l = 0
        r = 0
        while l<len(left) and r<len(right):
            if left[l] <= right[r]:
                arr.append(left[l])
                l += 1
            else:
                arr.append(right[r])
                r += 1
        
        for i in range(l, len(left)):
            arr.append(left[i])
        for i in range(r, len(right)):
            arr.append(right[i])
        
        return arr
   