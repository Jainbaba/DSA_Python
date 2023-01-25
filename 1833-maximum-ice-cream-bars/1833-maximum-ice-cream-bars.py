class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        i = 0
        currsum = 0
        while(i < len(costs) and currsum + costs[i] <= coins):
            currsum += costs[i]
            i += 1
        return i
            
            
 
 
            
        
        
        
        
        