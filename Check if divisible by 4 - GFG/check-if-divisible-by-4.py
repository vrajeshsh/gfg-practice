#User function Template for python3
class Solution:
	def divisibleBy4 (self, N):
		# Your Code Here
		return 1 if int(N[-2:])%4==0 else 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		print(ob.divisibleBy4(s))

		#  Contributed By: Pranay Bansa
# } Driver Code Ends