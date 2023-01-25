from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        h = Counter(tasks)
        res = 0
        for v in h.values():
            if v == 1:
                return -1
            if v % 3 == 0:
                res += v // 3
            else:
                res += v // 3 + 1
        return res

       
                    

        


        
        