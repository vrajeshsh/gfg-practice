#User function Template for python3

class Solution:
    def removeConsecutiveCharacter(self, S):
        # code here
        new_str=""
        for i in range( len(S)-1):
            if S[i+1]==S[i]:
                continue
            else:
                new_str+=S[i]
        return new_str+S[-1]
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        s = input()
        ob = Solution()
        print(ob.removeConsecutiveCharacter(s))

# } Driver Code Ends