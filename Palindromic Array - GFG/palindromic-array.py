# Your task is to complete this function
# Function should return True/False or 1/0

# Python3 implementation to check
# if an array is PalinArray or not

# Function to check if palindrome or not
def isPalindrome(N):
	str1 = "" + str(N)
	len1 = len(str1)
	for i in range(int(len1 / 2)):
		if (str1[i] != str1[len1 - 1 - i]):
			return False
	return True

# Function to check
# if an array is PalinArray or not
def PalinArray(arr, n):
	
	# Traversing each element of the array
	# and check if it is palindrome or not
	for i in range(n):
		ans = isPalindrome(arr[i])
		if (ans == False):
			return False
	return True

# This code is contributed by PrinciRaj1992

#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends