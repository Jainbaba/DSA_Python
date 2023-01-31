#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        minDiff = float("inf")
        for i in range(0,N):
            if (i+M-1) < N:
                minDiff = min(minDiff,A[i+M-1] - A[i])
            else:
                break
        return minDiff
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends