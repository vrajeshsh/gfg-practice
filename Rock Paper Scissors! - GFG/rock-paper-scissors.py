#User function Template for python3

class Solution:
    def gameResult(self, S):
        # code here
        if S[0]==S[1]:
            return "DRAW"
        if S[0]=="P" and S[1]=="R" or S[0]=="S" and S[1]=="P" or S[0]=="R" and S[1]=="S":
            return "A"
        else:
            return "B"
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.gameResult(s)
        print(ans)
# } Driver Code Ends