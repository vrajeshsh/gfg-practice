#User function Template for python3

class Solution:
    def count (self,s):
        # your code here
        up, low, dig, spl = 0, 0, 0, 0
        for i in s:
            if i.isupper():
                up+=1
            elif i.islower():
                low+=1
            elif i.isdigit():
                dig+=1
            else:
                spl+=1
        return up, low, dig, spl
#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    ob = Solution()
    res = ob.count (s)
    
    for i in res:
        print (i)
    
# Contributed By: Pranay Bansal

# } Driver Code Ends