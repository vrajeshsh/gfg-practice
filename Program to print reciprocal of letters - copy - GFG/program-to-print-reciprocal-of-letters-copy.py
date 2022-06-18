#User function Template for python3
class Solution:
    def reciprocalString(self, S):
        # code here
        new_str="" 
        for i in S:
            if ord(i)>=ord("A") and ord(i)<=ord("Z"):
                new_str+=chr((ord("A")+ord("Z"))-ord(i))
            elif ord(i)>=ord("a") and ord(i)<=ord("z"):
                new_str+=chr((ord("a")+ord("z"))-ord(i))
            else:
                new_str+=i
        return new_str
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        print(ob.reciprocalString(S))
# } Driver Code Ends