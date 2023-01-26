class Solution:
    def helper(self,h,visited,hasApple,idx):
        appletime = 0
        visited[idx] = True
        
        for i in h[idx]:
            if not visited[i]:
                appletime += self.helper(h,visited,hasApple,i)
        
        if idx == 0:
            return appletime
        
        if hasApple[idx] or appletime > 0:
            appletime += 2
            
        return appletime
    
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        h = [[] for _ in range(0,n)]
        for e1,e2 in edges:
            h[e1].append(e2)
            h[e2].append(e1)
        visited = [False] * n
        return self.helper(h,visited,hasApple,0)
            
        
        
       
    

        




        



