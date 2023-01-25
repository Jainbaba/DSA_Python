class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h = {}
        s = s.split(" ")
        if len(pattern) != len(s) or len(set(pattern)) != len(set(s)):
            return False
        for i,j in zip(pattern,s):
            if i in h and h[i] != j:
                return False
            h[i] = j
        return True


                
                

                

        
                
        
        
            