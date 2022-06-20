#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
		low, mid, hi = 0, 0, n-1
		while low<=hi:
		    mid = (low+hi)//2
		    if arr[mid]<k:
		        low = mid+1
            elif arr[mid]>k:
                hi = mid -1
            else:
                return mid
        return -1

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends