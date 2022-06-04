#User function Template for python3

class Solution:
    def scores(self, a, b, cc):
        # Update list cc of length 2 with cc[0] = ca and cc[1] = cb
        # Your code goes here
        c1 =  c2 = 0

        for i in range(len(a)):
            if a[i] > b[i]:
                c1 +=1
            elif(a[i] < b[i]):
                c2+= 1
        cc[0] = c1
        cc[1] = c2
        
    	

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
    	a = [int(x) for x in input().strip().split()]
    	b = [int(x) for x in input().strip().split()]
    	
    	cc = [0, 0]
    	ob=Solution()
    	ob.scores(a, b, cc)
    	print(*cc)
    	
    	T -= 1

if __name__ == "__main__":
    main()







# } Driver Code Ends