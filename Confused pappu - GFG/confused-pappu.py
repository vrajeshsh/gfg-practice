#User function Template for python3

class Solution:

    def findDiff(self, amount):
        # code here
        new_str=""
        for ch in str(amount):
            new_str+= "9" if ch=="6" else ch
                
        return int(new_str)-amount
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        amount = int(input())

        solObj = Solution()

        print(solObj.findDiff(amount))
# } Driver Code Ends