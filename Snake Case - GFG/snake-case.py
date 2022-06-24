class Solution:
    def snakeCase(self, S , n):
        # code here
        new_str=""
        for ch in S:
            
            
            if ch==' ':
                new_str+="_"
            elif ch.upper():
                new_str+=ch.lower()
            else:
                new_str+=ch
        return   new_str  

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        S=input()
        
        ob = Solution()
        print(ob.snakeCase(S , n))
# } Driver Code Ends