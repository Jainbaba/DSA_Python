import math 
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            if n == 1:
                return x
            res = helper(x,n//2)
            if n % 2 == 0:
                return res * res
            else:
                return x * res * res

        return helper(x,n) if n >= 0 else (1/helper(x,abs(n)))
            
        
        


        
         
        
            