#User function Template for python3
class Solution:
	def isSame(self, s):
		# code here
		count, dig=0, ""
		for ch in range(len(s)):
		    if s[ch].isalpha():
		        count+=1
	        if s[ch].isdigit():
	            dig+=s[ch]
        return 1 if int(dig)==count else 0
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.isSame(s)
		
		print(answer)


# } Driver Code Ends