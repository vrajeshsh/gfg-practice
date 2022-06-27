#User function Template for python3
class Solution:
	def search(self, X, Y):
		# code here
		pos=0
        for i in range(len(X)-len(Y)+1):
            if X[i:i+len(Y)] == Y:
                pos=i+1
        return pos if pos!=0 else -1
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x,y = input().split()

		ob = Solution()
		answer = ob.search(x, y)
		print(answer)

# } Driver Code Ends