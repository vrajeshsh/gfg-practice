#User function Template for python3
class Solution:

	def zigZag(self,arr, n):
		# code here
		flag = True
        for i in range(n-1):
            # "<" relation expected
            if flag is True:
                # If we have a situation like A > B > C,
                # we get A > C < B
                # by swapping B and C
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
                # ">" relation expected
            else:
                # If we have a situation like A < B < C,
                # we get A < C > B
                # by swapping B and C    
                if arr[i] < arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
            flag = bool(1 - flag)

#{ 
#  Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.zigZag(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends