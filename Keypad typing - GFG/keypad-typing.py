#User function Template for python3


#Function to find matching decimal representation of a string as on the keypad.
def printNumber(s,n):
   
    #CODE HERE
    new_str=""
    for ch in s:
        if ch in "abc":
            new_str+="2"
        elif ch in "def":
            new_str+="3"
        elif ch in "ghi":
            new_str+="4"
        elif ch in "jkl":
            new_str+="5"
        elif ch in "mno":
            new_str+="6"
        elif ch in "pqrs":
            new_str+="7"
        elif ch in "tuv":
            new_str+="8"
        elif ch in "wxyz":
            new_str+="9"
    return new_str
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        
        s=input()
        n=len(s)
        print(printNumber(s,n))
# } Driver Code Ends