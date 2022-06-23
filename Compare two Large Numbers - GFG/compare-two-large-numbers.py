#User function Template for python3

class Solution:

    def check(self, a,b):
        A, B = str(a), str(b)
        if (len(A) != len(B)):
            return 1 if len(A) < len(B) else 2
        for i in range(len(A)):
            if (ord(A[i]) < ord(B[i])): return 1
            if (ord(A[i]) > ord(B[i])): return 2
        return 3

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        a= int(input())
        b = int(input())

        solObj = Solution()

        print(solObj.check(a,b))
# } Driver Code Ends