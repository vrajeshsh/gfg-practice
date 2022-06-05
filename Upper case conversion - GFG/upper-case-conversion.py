#User function Template for python3

class Solution:
    def transform(self, s):
        # code here
        new_str=""
        for i in range(len(s)):
            if i==0 or s[i-1]==" ":
                new_str+=s[i].upper()
            else:
                new_str+=s[i]
        return new_str

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        print(ob.transform(s))
# } Driver Code Ends