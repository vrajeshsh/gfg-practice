#User function Template for python3


class Solution:
    def modify(self, s):
        # code here
        if ord(s[0])>=97:
            return s.lower()
        else:
            return s.upper()

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    print(ob.modify(s))
# } Driver Code Ends