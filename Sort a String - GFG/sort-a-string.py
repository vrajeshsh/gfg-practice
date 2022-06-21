#User function Template for python3
class Solution:
    def sort(self, s): 
        #code here
        new_str=""
        for i in range(97, 123):
            for ch in s:
                if i==ord(ch):
                    new_str+=ch
        return new_str
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        obj = Solution()
        ans = obj.sort(s)
        print(ans)
# } Driver Code Ends