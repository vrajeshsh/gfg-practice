#User function Template for python3

class Solution:
    def findIndex (self,a, N, key ):
        #code here.
        isFound = False
        count, count2 = -1, 0
        for i in a:
            count+=1
            if i==key:
                isFound=True
                break
        for i in a[::-1]:
            count2+=1
            if i==key:
                isFound=True
                break
        if not isFound:
            count, count2 = -1, N+1
        return count, N-count2
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    key=int(input())
    ob = Solution()
    ans=ob.findIndex(a, n, key )
    print(*ans)
    
# } Driver Code Ends