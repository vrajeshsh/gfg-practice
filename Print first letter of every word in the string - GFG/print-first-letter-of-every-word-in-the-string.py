#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
		new_str=""
		for i in range(len(S)):
		    if i==0 or S[i-1]==' ':
		        new_str+=S[i]
        return new_str

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.firstAlphabet(S)
		
		print(answer)


# } Driver Code Ends