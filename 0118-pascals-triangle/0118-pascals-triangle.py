class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        val = []
        for i in range(1,numRows+1):
            temp = [1] * i
            if val:
                j = 0
                while(j+1 < len(val[-1])):
                    temp[j+1] = val[-1][j] + val[-1][j+1] 
                    j += 1
                val.append(temp)
            else:
                val.append([1])
        return val
        