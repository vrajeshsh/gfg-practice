#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		if(n<2):
            return -1
        res=arr[0]
        sm=-1
        for i in range(n):
            if(arr[i]>res):
                res= arr[i]
        for i in range(n):
            if(arr[i]>sm and arr[i]<res):
                sm=arr[i]
        return sm
        
		

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends