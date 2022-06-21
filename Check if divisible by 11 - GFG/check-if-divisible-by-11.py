#User function Template for python3
class Solution:
	def divisibleBy11(self, S):
		# Your Code Here
        sign, ssum, num = 1, 0, int(S)
        while num>0:
            ssum+=(sign)*(num%10)
            sign*=-1
            num//=10
        return 1 if ((ssum/11)==(ssum//11)) or ssum==0 else 0
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		s = input ()
		ob = Solution()
		print (ob.divisibleBy11 (s)) 

# Contributed By: Pranay Bansal

# } Driver Code Ends