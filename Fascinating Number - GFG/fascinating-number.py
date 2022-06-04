#User function Template for python3
class Solution:

	def fascinating(self,n):
	    # code here
	    
	    a = n*2
	    b = n*3
	    str1 = str(n)+str(a)+str(b)
	    if len(str1)<=10:
    	    for i in range(1, 10):
    	        if str(i) not in str1:
    	            return False
            return True

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else:
            print("Not Fascinating")
        tc -= 1

# } Driver Code Ends