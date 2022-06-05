#User function Template for python3
class Solution:
	def removeVowels(self, S):
		# code here
		new_str=""
        for i in S:
            if i in "AEIOUaeiou":
                continue
            new_str+=i
        return new_str
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeVowels(s)
		
		print(answer)


# } Driver Code Ends