#User function Template for python3

def maxlength(s):
    count, maxi= 0, 0
    for ch in range(len(s)):
        if s[ch]=="1" and i!=len(s):
            count+=1
        else:
            if count>maxi:
                maxi = count
            count = 0
    return max(maxi, count)
    
    #add code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        s=input()
        print(maxlength(s))
# } Driver Code Ends