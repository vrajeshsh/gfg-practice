#User function Template for python3

class Solution:
	def streamAvg(self, arr, n):
		# code here
		ssum, arr2 = 0, []
        for i in range(n):
            ssum+=arr[i]
            arr2.append(ssum/(i+1))
        return arr2
#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends