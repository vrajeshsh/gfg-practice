#User function Template for python3

class Solution:
    def splitString(ob, S): 
        # code here 
       S1, S2, S3 = "", "", ""
       for chr in S:
           if chr.isalpha():
               S1+=chr
           elif chr.isdigit():
               S2+=chr
           else:
               S3+=chr
       return S1, S2, S3

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        ob = Solution()
        ans = ob.splitString(S)
        for i in ans:
            if(i==""):
                print(-1)
            else:
                print(i)


# } Driver Code Ends