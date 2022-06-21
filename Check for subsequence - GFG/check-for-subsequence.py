#User function Template for python3

class Solution:
    def isSubSequence(self, A, B):
        #code here
        ind=0
        for i in range(len(B)):
            if A[ind]==B[i]:
                ind+=1
            if len(A)==ind:
                return 1
        if len(A)==ind:
            return 1
        else:
            return 0

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        A,B = input().split()
        ob = Solution()
        if ob.isSubSequence(A,B):
            print(1)
        else:
            print(0)

# } Driver Code Ends