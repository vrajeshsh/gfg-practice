#User function Template for python3

class Solution:
    def removeSpecialCharacter (self, S):
		#code here
		new_str=""
		for ch in S:
		    if ch.isalpha():
		        new_str+=ch
		        
        return new_str if new_str!="" else -1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.removeSpecialCharacter(S))


# } Driver Code Ends