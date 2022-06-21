#User function Template for python3

class Solution:
    def LastIndex(self, s, p):
        # code here
        pos=0
        if p not in s:
            return -1
        for i in range(len(s)-1, 0, -1):
            if s[i]==p:
                pos=i
                break
        return pos

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        p = input().strip()[0]
        
        ob=Solution()
        print(ob.LastIndex(s, p))
# } Driver Code Ends