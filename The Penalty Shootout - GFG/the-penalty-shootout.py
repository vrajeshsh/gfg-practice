#User function Template for python3
class Solution:
	def penaltyScore(self, S):
		# code here
		count=0
		for ch in range(len(S)-1):
		    if S[ch]=="2" and S[ch+1]=="1":
		        count+=1
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.penaltyScore(S)
		
		print(answer)


# } Driver Code Ends