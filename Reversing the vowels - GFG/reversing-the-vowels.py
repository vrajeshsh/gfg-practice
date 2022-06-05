#User function Template for python3

class Solution:
    def modify(self, s):
        # code here
        a=list(s)
        c=0
        k=[]
        for i in range(len(a)):
            if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u"):
                k.append(a[i])
        
        k=list(reversed(k))
        for i in range(len(a)):
            if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u"):
                a[i]=k[c]
                c+=1
        ans=''
        ans=ans.join(a)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.modify(s)
        print(ans)
# } Driver Code Ends