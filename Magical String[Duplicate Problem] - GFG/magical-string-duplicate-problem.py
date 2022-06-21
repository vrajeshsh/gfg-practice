#User function Template for python3
class Solution:
    def magicalString (ob,S):
        # code here 
        new_str=""
        for ch in S:
            new_str+=chr(219-ord(ch))
        return new_str

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.magicalString(S))
# } Driver Code Ends