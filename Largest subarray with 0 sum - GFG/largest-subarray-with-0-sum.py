#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        sumi,maxi = 0,0
        h = {}
        for i in range(0,n):
            sumi += arr[i]
            if sumi == 0:
                maxi = i+1
                continue
            if sumi in h:
                maxi = max(i - h[sumi],maxi)
            else:
                h[sumi] = i
        return(maxi)


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends