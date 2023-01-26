class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        h = defaultdict(list)
        for idx,par in enumerate(parent):
            h[par].append(idx)
                    
        ans = 1
        def dfs(idx):
            nonlocal ans
            lar = seclar = 0
            for i in h[idx]:
                pathlen = dfs(i)
                if s[i] != s[idx]:
                    if pathlen > lar:
                        seclar = lar
                        lar = pathlen
                    elif pathlen > seclar:
                        seclar = pathlen
            ans = max(ans,lar+seclar+1)
            return lar+1
                
                
        dfs(0)
        return(ans)
        



            



        

        
        

            

        







        


