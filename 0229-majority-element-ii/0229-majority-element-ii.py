class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n1,n2 = float("-inf"),float("-inf")
        c1,c2 = 0,0
        for i in nums:
            if n1 == i:
                c1 += 1
            elif n2 == i:
                c2 += 1
            elif c1 == 0:
                n1 = i
                c1 = 1
            elif c2 == 0:
                n2 = i
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1         
        return [n for n in (n1, n2) if nums.count(n) > len(nums)// 3]