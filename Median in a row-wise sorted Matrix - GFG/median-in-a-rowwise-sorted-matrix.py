#User function Template for python3

class Solution:
    def countSmallerValue(self,row,mid):
        l = 0
        h = len(row)-1
        while(l<=h):
            m = (l + h) // 2
            if row[m] <= mid:
                l = m + 1
            else:
                h = m - 1
        return l
    
    def median(self, matrix, R, C):
        l = 1 
        h = 2000
        while(l <= h):
            mid = (l + h) // 2
            count = 0
            for i in range(0,R):
                count+= self.countSmallerValue(matrix[i],mid)
            if count <= ((R*C) // 2):
                l = mid + 1
            else:
                h = mid - 1
        return l
        
 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends