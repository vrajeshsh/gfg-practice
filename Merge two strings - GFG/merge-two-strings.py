#User function Template for python3
class Solution:
    def merge(self, S1, S2):
        # code here
        ans = ""
        i = 0 
        while i < min( len(S1) , len(S2)):
           ans += S1[i]
           ans += S2[i]
           i += 1
        while i < len(S1):
           ans += S1[i]
           i += 1
           
        while i < len(S2):
           ans += S2[i]
           i += 1
           
        return ans 
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S1,S2 = map(str,input().strip().split())
        ob = Solution()
        print(ob.merge(S1, S2))
# } Driver Code Ends