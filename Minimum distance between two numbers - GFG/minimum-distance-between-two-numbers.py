

class Solution:
    def minDist(self, arr, n, x, y):
        x1 = y1 = -1
        f1 = f2 = False
        dis = float("inf")
        
        for i in range(n):
            
            if arr[i] == x:
                x1 = i
                f1 = True
            
            elif arr[i] == y:
                y1 = i
                f2 = True
            
            if f1 and f2:
                dis = min(dis, abs(x1-y1))
                if arr[i] == x:
                    f2 = False
                elif arr[i] == y:
                    f1 = False
        
        return -1 if dis == float("inf") else dis
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends