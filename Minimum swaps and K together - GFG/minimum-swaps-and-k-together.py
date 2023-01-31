#User function Template for python3

class Solution:
        
    def minSwap (self,arr, n, k) :
        win = 0
        for i in range(0,n):
            if arr[i] <= k:
                win += 1
        
        count = 0
        swap = 0
        mini = float("inf")
        for i in range(0,n):
            if i < win:
                if arr[i] > k:
                    swap +=1
                mini = swap
            else:
                if arr[i-win] <= k and arr[i] > k:
                    swap += 1
                elif arr[i-win] > k and arr[i] <=k:
                    swap -= 1
                mini = min(mini,swap)

        return(mini)
                    
                    
                
            
        
            
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ob=Solution()
    ans = ob.minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends