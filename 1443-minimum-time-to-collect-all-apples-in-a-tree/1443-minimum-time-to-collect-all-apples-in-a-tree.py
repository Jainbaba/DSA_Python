from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        h = defaultdict(list)
        for e1,e2 in edges:
            h[e1].append(e2)
            h[e2].append(e1)

        def dfs(curr, par):
            curr_amount = 0
            for node in h[curr]:
                if node == par:
                    continue
                child = dfs(node, curr)
                if hasApple[node] or child > 0:
                    curr_amount += 2 + child
            return curr_amount

        return dfs(0,-1)
            
        
        
       
    

        




        



