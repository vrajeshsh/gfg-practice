#User function Template for python3

class Solution:
    def UncommonChars(self,A, B):
        #code here
        new_str, ans="", ""
        for ch in A:
            if ch not in B and ch not in new_str:
                new_str+=ch
        for ch in B:
            if ch not in A and ch not in new_str:
                new_str+=ch
        for ch in sorted(new_str):
            ans+=ch
        return ans if ans!="" else -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        A = input()
        B = input()
        ob = Solution()
        print(ob.UncommonChars(A, B))

# } Driver Code Ends